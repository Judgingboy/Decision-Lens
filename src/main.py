from agents.structure_agent import structure_decision
from core.attribute_mapper import map_attributes
from core.decision_engine import compute_weighted_scores
from utils.input_helpers import (
    get_weights_from_ranking,
    confirm_criteria_types,
    confirm_ordinal_scales,
    get_multiline_input,
    confirm_options,
    confirm_criteria,
    post_result_menu,
)

# 🔧 Debug flag - IF SET TO True-> it would be seen in terminal , IF SET TO False -> Hidden
DEBUG = True


def debug_state(criteria, weights, mapped_attributes):
    print("\n--- DEBUG STATE ---")
    print("Criteria:")
    for c, meta in criteria.items():
        print(f"  {c}: {meta}")

    print("\nWeights:")
    for c, w in weights.items():
        print(f"  {c}: {round(w, 3)}")

    print("\nMapped attributes:")
    for opt, vals in mapped_attributes.items():
        print(f"  {opt}: {vals}")

    print("-------------------\n")

def show_criteria_summary(criteria):  #To see criteria summary before ranking
    print("\nCriteria summary (for ranking):")
    for i, (c, meta) in enumerate(criteria.items(), start=1):
        ctype = meta["type"]
        unit = meta.get("unit")
        scale = meta.get("scale")

        if scale:
            print(
                f"{i}. {c} ({ctype}) → scale: "
                f"{' < '.join(scale)}"
            )
        else:
            unit_label = f", unit: {unit}" if unit else ""
            print(f"{i}. {c} ({ctype}{unit_label})")


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
    options = confirm_options(options, criteria)

    # 4. User confirms / edits CRITERIA
    criteria = confirm_criteria(criteria, options)

    # 5. User confirms cost vs benefit
    criteria = confirm_criteria_types(criteria)

    # 6. User confirms ordinal scales
    criteria = confirm_ordinal_scales(criteria, options)

    # Warn if criteria have no data across all options
    for c in criteria:
        if all(
            options.get(opt, {}).get(c) in (None, "unknown")
            for opt in options
        ):
            print(
                f"\nWarning: Some criteria have no data for any option. "
                "Results may be inconclusive."
            )
            break

    # 7. User ranks criteria (importance)
    criterion_names = list(criteria.keys())
    show_criteria_summary(criteria)
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

    # 10. Main evaluation loop
    while True:
        # Recompute results
        results = compute_weighted_scores(
            options=list(mapped_attributes.keys()),
            criteria=criterion_names,
            weights=weights,
            values=mapped_attributes,
            criteria_types=criteria_types
        )

        # 🔍 Debug output (always current)
        if DEBUG:
            debug_state(criteria, weights, mapped_attributes)

        # Show results
        print("\nRanked Results:")
        for option, score in results.items():
            print(f"{option}: {score}")

        # Post-result menu
        choice = post_result_menu()

        if choice == "0":
            print("\nDecision finalized. Exiting.")
            break

        elif choice == "1":
            weights = get_weights_from_ranking(criterion_names)

        elif choice == "2":
            options = confirm_options(options, criteria)
            mapped_attributes = map_attributes({
                "criteria": criteria,
                "options": options
            })

        elif choice == "3":
            criteria = confirm_criteria(criteria, options)
            criteria = confirm_criteria_types(criteria)
            criteria = confirm_ordinal_scales(criteria, options)

            criterion_names = list(criteria.keys())
            criteria_types = {
                c: meta["type"] for c, meta in criteria.items()
            }

            mapped_attributes = map_attributes({
                "criteria": criteria,
                "options": options
            })

            # 🔁 Ask if user wants to re-rank after changing criteria
            re_rank = input(
                "\nCriteria were modified. Do you want to re-rank their importance? (y/n): "
            ).strip().lower()

            if re_rank == "y":
                weights = get_weights_from_ranking(criterion_names)

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")