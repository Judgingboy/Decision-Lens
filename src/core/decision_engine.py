def compute_weighted_scores(options, criteria, weights, ratings, criteria_types):
    # Step 1: collect raw values per criterion
    criterion_values = {
        criterion: [ratings[opt][criterion] for opt in options]
        for criterion in criteria
    }

    # Step 2: normalize values
    normalized = {opt: {} for opt in options}

    for criterion in criteria:
        values = criterion_values[criterion]
        min_v = min(values)
        max_v = max(values)

        for opt in options:
            v = ratings[opt][criterion]

            # Avoid division by zero (all values equal)
            if max_v == min_v:
                norm = 1.0
            else:
                if criteria_types.get(criterion) == "cost":
                    norm = (max_v - v) / (max_v - min_v)
                else:  # benefit
                    norm = (v - min_v) / (max_v - min_v)

            normalized[opt][criterion] = norm

    # Step 3: weighted sum
    results = {}
    for opt in options:
        score = sum(
            normalized[opt][criterion] * weights[criterion]
            for criterion in criteria
        )
        results[opt] = round(score, 3)

    return dict(sorted(results.items(), key=lambda x: x[1], reverse=True))