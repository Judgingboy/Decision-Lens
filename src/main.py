from core.decision_engine import compute_weighted_scores
from core.validation import validate_weights, validate_ratings
from utils.input_helpers import get_list_from_user, get_weights, get_ratings

def main():
    options = get_list_from_user("Enter your options:")
    criteria = get_list_from_user("Enter evaluation criteria:")

    if not options or not criteria:
        print("Options and criteria cannot be empty.")
        return

    weights = get_weights(criteria)
    ratings = get_ratings(options, criteria)

    if not validate_ratings(options, criteria, ratings):
        print("Invalid ratings provided.")
        return

    results = compute_weighted_scores(options, criteria, weights, ratings)

    print("\nRanked Results:")
    for option, score in results.items():
        print(f"{option}: {score}")

if __name__ == "__main__":
    main()
