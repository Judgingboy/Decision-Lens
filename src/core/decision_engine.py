def compute_weighted_scores(options, criteria, weights, values, criteria_types):
    """
    Computes weighted scores with:
    - cost vs benefit handling
    - normalization across options
    - missing-value handling via per-option weight renormalization
    """

    # Step 1: collect raw values per criterion (ignore None)
    criterion_values = {}

    for criterion in criteria:
        vals = [
            values[opt][criterion]
            for opt in options
            if values[opt].get(criterion) is not None
        ]
        criterion_values[criterion] = vals

    # Step 2: normalize values per criterion
    normalized = {opt: {} for opt in options}

    for criterion in criteria:
        vals = criterion_values[criterion]

        # If nobody has data for this criterion, skip entirely
        if not vals:
            continue

        min_v = min(vals)
        max_v = max(vals)

        for opt in options:
            raw = values[opt].get(criterion)

            if raw is None:
                normalized[opt][criterion] = None
                continue

            # Avoid division by zero (all values equal)
            if max_v == min_v:
                norm = 1.0
            else:
                if criteria_types.get(criterion) == "cost":
                    norm = (max_v - raw) / (max_v - min_v)
                else:  # benefit
                    norm = (raw - min_v) / (max_v - min_v)

            normalized[opt][criterion] = norm

    # Step 3: compute weighted scores with per-option renormalization
    results = {}

    for opt in options:
        # Keep only criteria that have values for this option
        available_criteria = [
            c for c in criteria if normalized[opt].get(c) is not None
        ]

        # If nothing is available, score is zero
        if not available_criteria:
            results[opt] = 0.0
            continue

        # Renormalize weights
        total_weight = sum(weights[c] for c in available_criteria)
        effective_weights = {
            c: weights[c] / total_weight for c in available_criteria
        }

        # Compute score
        score = sum(
            normalized[opt][c] * effective_weights[c]
            for c in available_criteria
        )

        results[opt] = round(score, 3)

    return dict(sorted(results.items(), key=lambda x: x[1], reverse=True))

