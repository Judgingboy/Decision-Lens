from agents.structure_agent import structure_decision
from core.attribute_mapper import map_attributes
from core.decision_engine import compute_weighted_scores
from utils.input_helpers import (
    get_weights_from_ranking,
    confirm_criteria_types,
    confirm_ordinal_scales,
    get_multiline_input,
    confirm_options,
    confirm_criteria
)


def main():
    # 1. Multiline human input
    user_input = get_multiline_input(
        "Describe your decision problem:"
    )

    # 2. AI-assisted structuring (DRAFT)
    structured = structure_decision(user_input)

    criteria = structured.get("criteria", {})
    options = structured.get("options", {})

    if not criteria or not options:
        print("Could not extract sufficient decision structure.")
        return

    # 3. User confirms / edits OPTIONS
    options = confirm_options(options)

    # 4. User confirms / edits CRITERIA
    criteria = confirm_criteria(criteria)

    # 5. User confirms cost vs benefit
    criteria = confirm_criteria_types(criteria)

    # 6. User confirms ordinal scales
    criteria = confirm_ordinal_scales(criteria)

    # 7. User ranks criteria (importance)
    criterion_names = list(criteria.keys())
    weights = get_weights_from_ranking(criterion_names)

    # 8. Prepare criteria types for engine
    criteria_types = {
        c: meta["type"] for c, meta in criteria.items()
    }

    # 9. Attribute mapping (descriptors → numbers)
    mapped_attributes = map_attributes({
        "criteria": criteria,
        "options": options
    })

    # Debug (temporary)
    print("\nCriteria:", criteria)
    print("\nMapped attributes:", mapped_attributes)

    # 10. Deterministic scoring
    results = compute_weighted_scores(
        options=list(mapped_attributes.keys()),
        criteria=criterion_names,
        weights=weights,
        values=mapped_attributes,
        criteria_types=criteria_types
    )

    # 11. Output results
    print("\nRanked Results:")
    for option, score in results.items():
        print(f"{option}: {score}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")