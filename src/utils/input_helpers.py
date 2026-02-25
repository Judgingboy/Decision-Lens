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
    print("\nConfirm criteria types:")

    keys = list(criteria.keys())

    for i, c in enumerate(keys, start=1):
        print(f"{i}. {c} → {criteria[c]['type']}")

    while True:
        choice = input(
            "\nEnter criterion number to toggle (or 'done'): "
        ).strip().lower()

        if choice == "done":
            break

        if not choice.isdigit():
            continue

        idx = int(choice) - 1
        if idx < 0 or idx >= len(keys):
            continue

        key = keys[idx]
        current = criteria[key]["type"]
        criteria[key]["type"] = "benefit" if current == "cost" else "cost"

        print(f"{key} set to {criteria[key]['type']}")

    # Normalize keys BEFORE returning
    return {
        normalize_key(k): v for k, v in criteria.items()
    }

def confirm_ordinal_scales(criteria):
    """
    Allows the user to confirm or edit ordinal scales suggested by the Structure Agent.
    """
    normalized = {}

    for raw_key, meta in criteria.items():
        key = normalize_key(raw_key)
        normalized[key] = meta

        scale = meta.get("scale")
        #skip criteria without scales (numeric or unknown)
        if not scale:
            continue

        print("\nCriterion:", raw_key)
        print("Proposed order (worst → best):")
        for i, v in enumerate(scale, start=1):
            print(f"{i}. {v}")

        print(
            "\nThis order defines what is considered better for comparison."
        )
        choice = input("Is this order correct for you? (y/n): ").strip().lower()
        if choice == "y":
            continue
        # If not correct, allow user to input a new scale
        new_scale = input(
            "Enter corrected scale (comma-separated, lowest → highest): "
        ).strip()

        if new_scale:
            normalized[key]["scale"] = [
                s.strip() for s in new_scale.split(",")
            ]

    return normalized

def confirm_options(options: dict) -> dict:
    while True:
        print("\nIdentified options:")
        for i, opt in enumerate(options.keys(), start=1):
            print(f"{i}. {opt}")

        choice = input(
            "\n[a] Add option  [r] Remove option  [c] Continue: "
        ).strip().lower()

        if choice == "c":
            break

        elif choice == "a":
            name = input("Enter new option name: ").strip()
            if name:
                options[name] = {}

        elif choice == "r":
            idx = input("Enter option number to remove: ").strip()
            if idx.isdigit():
                i = int(idx) - 1
                if 0 <= i < len(options):
                    key = list(options.keys())[i]
                    options.pop(key)

    return options

from utils.normalization import normalize_key


def confirm_criteria(criteria: dict) -> dict:
    """
    Allows the user to add or remove criteria suggested by the Structure Agent.
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

            criteria[key] = {
                "type": "benefit" if ctype == "b" else "cost",
                "description": "User-added criterion",
                "scale": [],
                "unit": None
            }

        elif choice == "r":
            idx = input("Enter criterion number to remove: ").strip()
            if idx.isdigit():
                i = int(idx) - 1
                if 0 <= i < len(keys):
                    criteria.pop(keys[i])

    return criteria

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
