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


def get_weights(criteria):
    raw_weights = {}
    print("\nEnter importance for each criterion (any positive number):")

    for criterion in criteria:
        while True:
            try:
                value = float(input(f"{criterion}: "))
                if value > 0:
                    raw_weights[criterion] = value
                    break
                else:
                    print("Weight must be positive.")
            except ValueError:
                print("Please enter a number.")

    total = sum(raw_weights.values())
    weights = {k: v / total for k, v in raw_weights.items()}

    return weights


def get_ratings(options, criteria):
    ratings = {}
    print("\nRate each option for each criterion (1–10):")

    for option in options:
        print(f"\nOption: {option}")
        ratings[option] = {}

        for criterion in criteria:
            while True:
                try:
                    score = float(input(f"  {criterion}: "))
                    if 1 <= score <= 10:
                        ratings[option][criterion] = score
                        break
                    else:
                        print("Score must be between 1 and 10.")
                except ValueError:
                    print("Please enter a number.")

    return ratings
