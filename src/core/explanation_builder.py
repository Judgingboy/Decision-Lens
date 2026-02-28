from utils.normalization import normalize_key


def build_explanation_payload(
    results: dict,
    normalized_values: dict,
    raw_values: dict,
    criteria: dict,
    weights: dict
) -> dict:
    """
    Builds a deterministic explanation payload from engine outputs.
    Contains ONLY factual, auditable data.
    """

    ranked_options = list(results.keys())

    # Top user priorities (highest weights)
    user_priorities = sorted(
        weights.keys(),
        key=lambda c: weights[c],
        reverse=True
    )[:3]

    payload = {
        "summary": {},
        "options": {},
        "user_priorities": user_priorities
    }

    # ---- Summary ----
    if len(ranked_options) > 1:
        top = ranked_options[0]
        second = ranked_options[1]
        payload["summary"] = {
            "top_option": top,
            "score_gap_to_next": round(results[top] - results[second], 3)
        }
    else:
        payload["summary"] = {
            "top_option": ranked_options[0],
            "score_gap_to_next": None
        }

    # ---- Per-option explanation ----
    for rank, option in enumerate(ranked_options, start=1):
        positive = {}
        negative = {}
        missing = []

        option_norm_vals = normalized_values.get(option, {})

        for raw_criterion, meta in criteria.items():
            c = normalize_key(raw_criterion)
            norm_val = option_norm_vals.get(c)

            if norm_val is None:
                missing.append(raw_criterion)
                continue

            weight = weights.get(raw_criterion, 0)
            contribution = norm_val * weight

            if meta["type"] == "cost":
                negative[raw_criterion] = contribution
            else:
                positive[raw_criterion] = contribution

        payload["options"][option] = {
            "rank": rank,
            "score": round(results[option], 3),
            "top_positive_factors": sorted(
                positive,
                key=positive.get,
                reverse=True
            )[:3],
            "top_negative_factors": sorted(
                negative,
                key=negative.get,
                reverse=True
            )[:3],
            "missing_criteria": missing,
            "applied_weights": {
                c: weights[c]
                for c in set(
                    list(positive.keys())[:3] +
                    list(negative.keys())[:3]
                )
            }
        }

    return payload