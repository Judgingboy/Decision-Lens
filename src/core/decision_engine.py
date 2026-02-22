def compute_weighted_scores(options, criteria, weights, ratings, criteria_types=None):
    results = {}

    for option in options:
        total_score = 0
        for criterion in criteria:
            score = ratings[option][criterion]
            
            # If it's a cost (lower is better), invert the 1-10 scale
            if criteria_types and criteria_types.get(criterion) == "cost":
                score = 11 - score
                
            total_score += score * weights[criterion]
        results[option] = round(total_score, 3)

    return dict(sorted(results.items(), key=lambda x: x[1], reverse=True))
