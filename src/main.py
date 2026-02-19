from core.decision_engine import compute_weighted_scores
from core.validation import validate_weights, validate_ratings

options = ["Laptop A", "Laptop B", "Laptop C"]
criteria = ["Price", "Performance", "Battery"]

weights = {
    "Price": 0.3,
    "Performance": 0.4,
    "Battery": 0.3
}

ratings = {
    "Laptop A": {"Price": 8, "Performance": 6, "Battery": 7},
    "Laptop B": {"Price": 6, "Performance": 9, "Battery": 8},
    "Laptop C": {"Price": 9, "Performance": 5, "Battery": 6}
}

assert validate_weights(weights)
assert validate_ratings(options, criteria, ratings)

results = compute_weighted_scores(options, criteria, weights, ratings)

print("Ranked Results:")
for option, score in results.items():
    print(option, score)
