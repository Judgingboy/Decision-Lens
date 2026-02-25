def get_list_from_user(prompt):
    items = []
    print(prompt)
    print("Type 'done' when finished.\n")

    while True:
        value = input("> ").strip()
        if value.lower() == "done":
            break
        if value:
            items.append(value)

    return items

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

    for i, (c, meta) in enumerate(criteria.items(), start=1):
        print(f"{i}. {c} → {meta['type']}")

    while True:
        choice = input(
            "\nEnter criterion number to toggle (or 'done'): "
        ).strip().lower()

        if choice == "done":
            break

        if not choice.isdigit():
            continue

        idx = int(choice) - 1
        if idx < 0 or idx >= len(criteria):
            continue

        key = list(criteria.keys())[idx]
        current = criteria[key]["type"]
        criteria[key]["type"] = "benefit" if current == "cost" else "cost"

        print(f"{key} set to {criteria[key]['type']}")

    return criteria

def confirm_ordinal_scales(criteria):
    """
    Allows the user to confirm or edit ordinal scales suggested by the Structure Agent.
    """

    for criterion, meta in criteria.items():
        scale = meta.get("scale")

        # Skip criteria without ordinal scales (numeric-only)
        if not scale:
            continue

        print(f"\nCriterion: {criterion}")
        print("Proposed scale (lowest → highest):")

        for i, value in enumerate(scale, start=1):
            print(f"{i}. {value}")

        choice = input("Is this scale correct? (y/n): ").strip().lower()

        if choice == "y":
            continue

        # User wants to edit
        new_scale = input(
            "Enter corrected scale (comma-separated, lowest → highest): "
        ).strip()

        if new_scale:
            meta["scale"] = [s.strip() for s in new_scale.split(",")]

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
