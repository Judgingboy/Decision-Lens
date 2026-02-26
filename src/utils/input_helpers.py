from utils.normalization import normalize_key

def get_multiline_input(prompt: str, end_token: str = "done") -> str:
    print(prompt)
    print(f"Type '{end_token}' on a new line when finished.\n")

    lines = []

    while True:
        line = input("> ")
        if line.strip().lower() == end_token:
            break
        lines.append(line)

    return "\n".join(lines)

# def get_list_from_user(prompt):  #Depreciated in favor of more structured input methods
#     items = []
#     print(prompt)
#     print("Type 'done' when finished.\n")

#     while True:
#         value = input("> ").strip()
#         if value.lower() == "done":
#             break
#         if value:
#             items.append(value)

#     return items

def get_criteria_from_user(prompt):
    criteria = []
    criteria_types = {}

    print(prompt)
    print("Type 'done' when finished.\n")

    while True:
        criterion = input("> ").strip()
        if criterion.lower() == "done":
            break
        if not criterion:
            continue

        criteria.append(criterion)

        while True:
            ctype = input(
                f'Is "{criterion}" a benefit or cost? (b = benefit, c = cost): '
            ).lower()

            if ctype == "b":
                criteria_types[criterion] = "benefit"
                break
            elif ctype == "c":
                criteria_types[criterion] = "cost"
                break
            else:
                print("Please enter 'b' or 'c'.")

    return criteria, criteria_types


def get_weights_from_ranking(criteria):
    rankings = {}
    print("\nRank criteria by importance (1 = highest priority):")

    for criterion in criteria:
        while True:
            try:
                rank = int(input(f"{criterion}: "))
                if 1 <= rank <= len(criteria):
                    rankings[criterion] = rank
                    break
                else:
                    print(f"Enter a number between 1 and {len(criteria)}.")
            except ValueError:
                print("Please enter a valid integer.")

    max_rank = len(criteria)
    raw_weights = {
        c: (max_rank + 1) - r
        for c, r in rankings.items()
    }

    total = sum(raw_weights.values())
    weights = {c: w / total for c, w in raw_weights.items()}

    return weights

def confirm_criteria_types(criteria):
    """
    Allows user to confirm or toggle cost/benefit classification.
    Reprints state after every change for clarity.
    """

    while True:
        print("\nConfirm criteria types:")
        keys = list(criteria.keys())

        for i, c in enumerate(keys, start=1):
            print(f"{i}. {c} → {criteria[c]['type']}")
        print("\nType numbers to toggle, 'done' when satisfied.")
        choice = input(
            "\nEnter criterion number to toggle (or 'done'): "
        ).strip().lower()

        if choice == "done":
            break

        if not choice.isdigit():
            print("Please enter a valid number or 'done'.")
            continue

        idx = int(choice) - 1
        if idx < 0 or idx >= len(keys):
            print("Invalid choice.")
            continue

        key = keys[idx]
        current = criteria[key]["type"]
        criteria[key]["type"] = "benefit" if current == "cost" else "cost"

        print(f"\n✔ {key} set to {criteria[key]['type']}")

    return criteria

def confirm_ordinal_scales(criteria: dict, options: dict) -> dict:
    """
    Allows the user to confirm or edit ordinal scales suggested by the Structure Agent.
    Resolves scale mismatches using explicit user choices.
    """

    for raw_key, meta in criteria.items():
        key = normalize_key(raw_key)
        scale = meta.get("scale")

        # Skip numeric or non-ordinal criteria
        if not scale:
            continue

        # ---- Step 1: Confirm proposed scale ----
        print("\nCriterion:", raw_key)
        print("Proposed order (worst → best):")
        for i, v in enumerate(scale, start=1):
            print(f"{i}. {v}")

        print("\nThis order defines what is considered better for comparison.")
        choice = input("Is this order correct for you? (y/n): ").strip().lower()

        if choice != "y":
            new_scale = input(
                "Enter corrected scale (comma-separated, lowest → highest): "
            ).strip()
            if new_scale:
                scale = [s.strip() for s in new_scale.split(",")]
                meta["scale"] = scale

        # ---- Step 2: Detect descriptor mismatches ----
        detected = set()
        for opt_vals in options.values():
            val = opt_vals.get(key)
            if isinstance(val, str):
                detected.add(normalize_key(val))

        scale_norm = {normalize_key(s) for s in meta["scale"]}
        missing = detected - scale_norm

        # ---- Step 3: Resolve mismatches explicitly ----
        if missing:
            updated_scale, alias_map, ignored = resolve_scale_mismatch(
                criterion_name=raw_key,
                scale=meta["scale"],
                unknown_values=missing
            )

            meta["scale"] = updated_scale

            # Store alias & ignored values for mapper
            if alias_map:
                meta.setdefault("aliases", {}).update(alias_map)

            if ignored:
                meta.setdefault("ignored_values", set()).update(ignored)

    return criteria

def confirm_options(options: dict, criteria: dict) -> dict:
    while True:
        print("\nIdentified options:")
        keys = list(options.keys())

        for i, opt in enumerate(keys, start=1):
            print(f"{i}. {opt}")

        choice = input(
            "\n[a] Add option  [r] Remove option  [c] Continue: "
        ).strip().lower()

        if choice == "c":
            break

        elif choice == "a":
            name = input("Enter new option name: ").strip()
            if not name:
                continue

            options[name] = {}
            print(f"\nEnter attributes for {name} (press Enter to skip):")

            for raw_c, meta in criteria.items():
                c = normalize_key(raw_c)
                scale = meta.get("scale")
                unit = meta.get("unit")

                # Build clear prompt
                if scale:
                    prompt = f"  {raw_c} (choose from: {', '.join(scale)}): "
                else:
                    unit_label = f", unit: {unit}" if unit else ""
                    prompt = f"  {raw_c} (enter number only{unit_label}): "

                while True:
                    val = input(prompt).strip()

                    # Allow skip
                    if not val:
                        break

                    # Ordinal criterion
                    if scale:
                        norm_val = normalize_key(val)
                        scale_norm = [normalize_key(s) for s in scale]

                        if norm_val not in scale_norm:
                            print(
                                f"  Invalid value. Allowed: {', '.join(scale)}"
                            )
                            continue

                        options[name][c] = val
                        break

                    # Numeric criterion
                    else:
                        try:
                            options[name][c] = float(val)
                            break
                        except ValueError:
                            print(
                                "  Invalid value. Please enter a number only."
                            )

        elif choice == "r":
            idx = input("Enter option number to remove: ").strip()
            if idx.isdigit():
                i = int(idx) - 1
                if 0 <= i < len(keys):
                    options.pop(keys[i])

    return options


def confirm_criteria(criteria: dict, options: dict) -> dict:
    """
    Allows the user to add or remove criteria.
    If a new criterion is added, immediately asks for values
    for all existing options.
    """

    while True:
        print("\nIdentified criteria:")
        keys = list(criteria.keys())

        for i, k in enumerate(keys, start=1):
            ctype = criteria[k].get("type", "unknown")
            print(f"{i}. {k} ({ctype})")

        choice = input(
            "\n[a] Add criterion  [r] Remove criterion  [c] Continue: "
        ).strip().lower()

        if choice == "c":
            break

        elif choice == "a":
            name = input("Enter criterion name: ").strip()
            if not name:
                continue

            key = normalize_key(name)

            ctype = input(
                "Is this a benefit or cost? (b = benefit, c = cost): "
            ).strip().lower()

            unit = input(
                "Enter unit (or press Enter if not applicable): "
            ).strip()

            criteria[key] = {
                "type": "benefit" if ctype == "b" else "cost",
                "description": "User-added criterion",
                "scale": [],
                "unit": unit if unit else None
            }

            # NEW PART: ask values for all existing options
            print(f"\nEnter values for new criterion '{name}' (press Enter to skip):")

            for opt, attrs in options.items():
                unit_label = f", unit: {unit}" if unit else ""
                prompt = f"  {opt} (enter number only{unit_label}): "

                while True:
                    val = input(prompt).strip()
                    if not val:
                        break

                    try:
                        attrs[key] = float(val)
                        break
                    except ValueError:
                        print("  Invalid value. Please enter a number only.")

        elif choice == "r":
            idx = input("Enter criterion number to remove: ").strip()
            if idx.isdigit():
                i = int(idx) - 1
                if 0 <= i < len(keys):
                    criteria.pop(keys[i])

    return criteria

def resolve_scale_mismatch(
    criterion_name: str,
    scale: list[str],
    unknown_values: set[str]
) -> tuple[list[str], dict[str, str], set[str]]:
    """
    Returns:
    - updated_scale
    - alias_map (e.g. {"mostly_good": "okay"})
    - ignored_values
    """
    alias_map = {}
    ignored = set()

    for val in unknown_values:
        print(f'\nThe value "{val}" is not in the scale.')

        while True:
            choice = input(
                "\nChoose how to resolve this:\n"
                "[a] Add to scale\n"
                "[m] Map to existing value\n"
                "[i] Ignore this value\n"
                "[e] Edit entire scale\n"
                "Choice: "
            ).strip().lower()

            # ADD TO SCALE
            if choice == "a":
                print("\nCurrent scale (lowest → highest):")
                for i, s in enumerate(scale, start=1):
                    print(f"{i}. {s}")

                pos = input(
                    f"Insert '{val}' at position (1–{len(scale)+1}): "
                ).strip()

                if pos.isdigit():
                    idx = int(pos) - 1
                    if 0 <= idx <= len(scale):
                        scale.insert(idx, val)
                        break

            # MAP TO EXISTING
            elif choice == "m":
                print("\nMap to:")
                for i, s in enumerate(scale, start=1):
                    print(f"{i}. {s}")

                sel = input("Choose number: ").strip()
                if sel.isdigit():
                    idx = int(sel) - 1
                    if 0 <= idx < len(scale):
                        alias_map[val] = scale[idx]
                        break

            # IGNORE
            elif choice == "i":
                ignored.add(val)
                break

            # EDIT ENTIRE SCALE
            elif choice == "e":
                new_scale = input(
                    "Enter new scale (comma-separated, lowest → highest): "
                ).strip()
                if new_scale:
                    scale[:] = [s.strip() for s in new_scale.split(",")]
                    break

    return scale, alias_map, ignored

# def prompt_missing_attributes(options: dict, criteria: dict) -> dict:
#     print("\nEnter attributes for options (press Enter to skip):")

#     for option, attrs in options.items():
#         print(f"\nOption: {option}")

#         for raw_c, meta in criteria.items():
#             c = normalize_key(raw_c)

#             # Skip if already present
#             if c in attrs:
#                 continue

#             unit = meta.get("unit")
#             label = f"{raw_c} ({unit})" if unit else raw_c

#             val = input(f"  {label}: ").strip()
#             if val:
#                 # Try numeric first, else keep string
#                 try:
#                     val = float(val)
#                 except ValueError:
#                     pass

#                 attrs[c] = val

#     return options

# def get_ratings(options, criteria):    #Depreciated in favor of more structured input methods
#     ratings = {}
#     print("\nRate each option for each criterion (1–10):")

#     for option in options:
#         print(f"\nOption: {option}")
#         ratings[option] = {}

#         for criterion in criteria:
#             while True:
#                 try:
#                     score = float(input(f"  {criterion}: "))
#                     if 1 <= score <= 10:
#                         ratings[option][criterion] = score
#                         break
#                     else:
#                         print("Score must be between 1 and 10.")
#                 except ValueError:
#                     print("Please enter a number.")

#     return ratings
