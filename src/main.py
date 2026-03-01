import textwrap
from agents.structure_agent import structure_decision
from agents.explanation_agent import render_explanation
from core.attribute_mapper import map_attributes
from core.decision_engine import compute_weighted_scores
from core.explanation_builder import build_explanation_payload
from utils.input_helpers import (
    get_weights_from_ranking,
    confirm_criteria_types,
    confirm_ordinal_scales,
    get_multiline_input,
    confirm_options,
    confirm_criteria,
    post_result_menu,
    resolve_empty_scaled_criteria,
    prompt_missing_values_for_criterion
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
    print(textwrap.dedent(r"""
        ██████╗ ███████╗ ██████╗██╗███████╗██╗ ██████╗ ███╗   ██╗    ██╗     ███████╗███╗   ██╗███████╗
        ██╔══██╗██╔════╝██╔════╝██║██╔════╝██║██╔═══██╗████╗  ██║    ██║     ██╔════╝████╗  ██║██╔════╝
        ██║  ██║█████╗  ██║     ██║███████╗██║██║   ██║██╔██╗ ██║    ██║     █████╗  ██╔██╗ ██║███████╗
        ██║  ██║██╔══╝  ██║     ██║╚════██║██║██║   ██║██║╚██╗██║    ██║     ██╔══╝  ██║╚██╗██║╚════██║
        ██████╔╝███████╗╚██████╗██║███████║██║╚██████╔╝██║ ╚████║    ███████╗███████╗██║ ╚████║███████║
        ╚═════╝ ╚══════╝ ╚═════╝╚═╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝    ╚══════╝╚══════╝╚═╝  ╚═══╝╚══════╝
    """))
    print("Decision Companion System")    
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

    # 🔧 FIX: Mark pre-existing scales as AUTO unless user explicitly set them
    for meta in criteria.values():
        if meta.get("scale") and "scale_source" not in meta:
            meta["scale_source"] = "auto"

    # 🔎 Handle ordinal criteria with USER-defined scales that have no values
    for c, meta in criteria.items():

        # Only care about USER-defined scales
        if meta.get("scale_source") != "user":
            continue

        # Skip ignored criteria
        if meta.get("ignored"):
            continue

        # Check if all options lack values
        if all(
            options.get(opt, {}).get(c) in (None, "unknown")
            for opt in options
        ):
            print(
                f"\n⚠ You defined a scale for '{c}', but no options have values for it."
            )
            print("Would you like to:")
            print("[1] Enter values now")
            print("[2] Ignore this criterion")

            choice = input("Choice (default = 2): ").strip() or "2"

            if choice == "1":
                prompt_missing_values_for_criterion(
                    criterion=c,
                    criteria=criteria,
                    options=options
                )
            else:
                meta["ignored"] = True
                print(f"✔ '{c}' has been ignored.")
    # 6.1 Resolve scaled criteria with no data
    criteria = resolve_empty_scaled_criteria(criteria, options)


    # Warn only for non-ignored criteria that still have no data
    empty_criteria = [
        c for c, meta in criteria.items()
        if not meta.get("ignored")
        and all(
            options.get(opt, {}).get(c) in (None, "unknown")
            for opt in options
        )
    ]

    if empty_criteria:
        print("\n⚠ Warning:")
        print(
            "The following criteria have no data for any option "
            "and may reduce result quality:"
        )
        for c in empty_criteria:
            print(f" - {c}")

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
        # Compute scores (deterministic core)
        results, normalized = compute_weighted_scores(
            options=list(mapped_attributes.keys()),
            criteria=criterion_names,
            weights=weights,
            values=mapped_attributes,
            criteria_types=criteria_types
        )

        # 🔍 Build deterministic explanation payload (NO AI)
        explanation_payload = build_explanation_payload(
            results=results,
            normalized_values=normalized,
            raw_values=mapped_attributes,
            criteria=criteria,
            weights=weights
        )
        
        # 🔍 Debug output (always current)
        if DEBUG:
            debug_state(criteria, weights, mapped_attributes)
            print("\n--- Explanation Payload ---")
            print(explanation_payload)
            print("---------------------------\n")


        # Show results
        print("\nRanked Results:")
        for option, score in results.items():
            print(f"{option}: {score}")

        #11. AI-generated explanation (DRAFT)
        explanation_text = render_explanation(explanation_payload)
        print("\n--- Explanation ---")
        print(explanation_text)
        print("-------------------\n")


        # Post-result menu
        choice = post_result_menu()

        if choice == "0":
            print("\nDecision finalized. Exiting.")
            break

        elif choice == "1":
            print("\nYou are re-ranking criteria importance based on current setup.")
            show_criteria_summary(criteria)
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

            # 🔥 REQUIRED: handle newly created USER scales with no values
            criteria = resolve_empty_scaled_criteria(criteria, options)

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
                print("\nRe-ranking criteria after changes:")
                show_criteria_summary(criteria)
                weights = get_weights_from_ranking(criterion_names)

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")