# Decision-Lens

## Understanding of the Problem
The objective of this project is to design and build a Decision Companion System that helps users make better, more informed decisions.

Rather than making decisions on behalf of the user, the system acts as a supportive tool that assists users in evaluating multiple options against clearly defined criteria. It makes trade-offs explicit and presents a ranked recommendation along with an explanation of why a particular option ranks higher.

The system is intentionally designed to not rely entirely on an AI model. While AI can be used to assist users—especially when they are unsure about inputs—the core decision-making logic remains deterministic, transparent, and explainable. If AI is used, its role and limitations are clearly defined and documented.

## Assumptions Made
- Users may already have a clear idea of their options and evaluation criteria.
- Some users may be unsure or “clueless” about how to structure their decision.
- When users are unsure, AI can optionally assist by suggesting options, criteria, or provisional scores.
- Users always retain control and can manually override or provide inputs at any stage.
- All final rankings are produced using deterministic logic, regardless of whether AI assistance was used earlier.
- Ratings are normalized on a fixed 1–10 scale, where higher values always indicate better performance. Cost-based criteria 
- Cost-based criteria such as price are evaluated in terms of value for money, not raw cost.

## Why the Solution Is Structured This Way
The solution is structured around a weighted decision-making approach. Each option is evaluated against multiple criteria, where:
- Each criterion has an associated weight representing its importance.
- Each option receives a rating for every criterion.

The final score of an option is calculated as the weighted sum of its ratings. This approach was chosen because it is:
- Simple and well-established
- Explainable and auditable
- Flexible across different decision domains
- Easy for users to understand and modify

This structure ensures that the system helps users reason about trade-offs rather than hiding logic behind a black box.

## Design Decisions and Trade-offs

### Data Structures Used
```python
options: list[str]
criteria: list[str]
weights: dict[str, float]
ratings: dict[str, dict[str, float]] # option -> criterion -> score
```

### Rationale
- **Lists** are used for options and criteria because they are ordered, mutable, and easy to extend or modify.
- **Dictionaries** are used for weights and ratings to allow clear mapping between criteria and their corresponding values.
- This combination provides readability, flexibility, and straightforward validation.
- The structure maps directly to the weighted scoring formula, keeping the implementation simple and explainable.

## Edge Cases Considered
- User does not provide valid or sufficient options.
- User-provided weights do not sum to 1.
- Missing weights for one or more criteria.
- Incomplete ratings (an option missing a rating for a criterion).
- Users unable to rate options, requiring AI-assisted provisional scoring.

All these cases are validated explicitly to prevent incorrect or misleading results.

## How to Run the Project
The project is a dynamic CLI-based Python application that guides you through the decision-making process.

**Basic steps:**
1. Clone the repository
2. Run the main Python script:
   ```bash
   python src/main.py
   ```
3. **Interactive Process:**
   - **Input Options:** List the items you are choosing between (e.g., Laptop A, Laptop B).
   - **Input Criteria:** Define what matters to you (e.g., Price, Performance).
   - **Assign Weights:** Enter a positive number for each criterion. The system automatically normalizes these so they sum to 1, allowing you to focus on relative importance.
   - **Rate Options:** Provide a score from 1 to 10 for each option across all criteria.

## What I Would Improve With More Time
While the system now supports dynamic user input, further improvements could include:
- Integration with LLMs for AI-assisted criteria and option discovery.
- Persistence layer to save and compare different decision sessions.
- Data visualization (e.g., bar charts or radar charts) for better comparison.
- Robust error handling for edge-case CLI inputs.
- Migration to a web-based interface for better accessibility.
