def compute_weighted_scores(options, criteria, weights, ratings):
    results = {}

    for option in options:
        total_score = 0
        for criterion in criteria:
            total_score += ratings[option][criterion] * weights[criterion]
        results[option] = round(total_score, 3)

    return dict(sorted(results.items(), key=lambda x: x[1], reverse=True))
