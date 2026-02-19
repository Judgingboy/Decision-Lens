def validate_weights(weights):
    return abs(sum(weights.values()) - 1.0) < 1e-6


def validate_ratings(options, criteria, ratings):
    for option in options:
        if option not in ratings:
            return False
        for criterion in criteria:
            if criterion not in ratings[option]:
                return False
    return True
