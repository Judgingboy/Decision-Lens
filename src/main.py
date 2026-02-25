# from core.decision_engine import compute_weighted_scores
# from core.validation import  validate_ratings
# from utils.input_helpers import get_list_from_user, get_criteria_from_user, get_weights_from_ranking, get_ratings

# def main():
#     options = get_list_from_user("Enter your options:")
#     criteria, criteria_types = get_criteria_from_user("Enter evaluation criteria:")

#     if not options or not criteria:
#         print("Options and criteria cannot be empty.")
#         return

#     weights = get_weights_from_ranking(criteria)
#     ratings = get_ratings(options, criteria)

#     if not validate_ratings(options, criteria, ratings):
#         print("Invalid ratings provided.")
#         return

#     results = compute_weighted_scores(options, criteria, weights, ratings, criteria_types)

#     print("\nRanked Results:")
#     for option, score in results.items():
#         print(f"{option}: {score}")

# if __name__ == "__main__":
#     try:
#         main()
#     except KeyboardInterrupt:
#         print("\n\nOperation cancelled by user.")


from agents.structure_agent import structure_decision
from core.attribute_mapper import map_attributes
from core.decision_engine import compute_weighted_scores
from utils.input_helpers import (
    get_list_from_user,
    get_weights_from_ranking,
    confirm_criteria_types,
    confirm_ordinal_scales
)


def main():
    print("Describe your decision problem:\n")
    user_input = input("> ")

    # 1. AI-assisted structuring (DRAFT)
    structured = structure_decision(user_input)

    criteria = structured.get("criteria", {})
    options = structured.get("options", {})

    if not criteria or not options:
        print("Could not extract sufficient decision structure.")
        return

    # 2. User confirms cost vs benefit
    criteria = confirm_criteria_types(criteria)

    # 3. User confirms ordinal scales
    criteria = confirm_ordinal_scales(criteria)

    # 4. User ranks criteria (importance)
    criterion_names = list(criteria.keys())
    weights = get_weights_from_ranking(criterion_names)

    # 5. Prepare criteria types for engine
    criteria_types = {
        c: meta["type"] for c, meta in criteria.items()
    }

    # 6. Attribute mapping (descriptors → numbers)
    mapped_attributes = map_attributes({
        "criteria": criteria,
        "options": options
    })

    print("\nMapped attributes:")  # Debug
    print(mapped_attributes)

    # 7. Deterministic scoring
    results = compute_weighted_scores(
        options=list(mapped_attributes.keys()),
        criteria=criterion_names,
        weights=weights,
        values=mapped_attributes,
        criteria_types=criteria_types
    )

    # 8. Output results
    print("\nRanked Results:")
    for option, score in results.items():
        print(f"{option}: {score}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")