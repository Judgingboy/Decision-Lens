# Decision-Lens

## Understanding of the Problem
The goal of this project is to build a Decision Companion System that helps users reason through complex, real-world decisions in a structured and transparent way.

Many decisions involve multiple options, competing criteria, incomplete information, and subjective preferences. Users often struggle not because they lack intelligence, but because the decision space itself is unstructured and the trade-offs are unclear. This system is designed to organize that chaos, not to replace human judgment.

Instead of making decisions on behalf of the user, the system assists the user by:

- Structuring messy, natural-language input into explicit options and criteria
- Making trade-offs visible through weighted evaluation
- Producing a ranked outcome along with a clear explanation of why that outcome occurred

A key requirement of the problem is trust. For a decision aid to be useful, users must be able to understand how and why a result was produced. For this reason, the system deliberately avoids using AI to score, rank, or guess outcomes. All scoring and ranking logic is deterministic, auditable, and repeatable.

AI is used only where it adds value without compromising trust—such as helping structure user input or converting deterministic results into human-readable explanations. Its role is strictly constrained, and it is never allowed to invent criteria, modify weights, or influence the final decision logic.
In short, the problem is not “choosing the best option,” but helping users make sense of their own priorities and constraints in a clear, explainable way. This project addresses that problem by combining structured decision logic with carefully limited AI assistance.

## Assumptions Made
- Users may approach the system with varying levels of clarity. Some users already know their options and criteria, while others may have only a vague idea of what they want.

- The system assumes that not all information will be available upfront. Users may skip values, be unsure about exact numbers, or prefer qualitative descriptions (e.g., “high”, “low”, “decent”) instead of precise data.
Ordinal (qualitative) judgments can be meaningfully converted into numeric representations as long as the relative ordering is explicitly defined by the user.

- When users are unsure how to structure their decision, AI assistance may be used optionally to help extract options and criteria from free-form input. This assistance is advisory and never authoritative.

- Users always retain full control over the decision model. They can add, remove, edit, or override options, criteria, scales, and values at any stage of the process.

- All final rankings are generated using deterministic, transparent logic. AI is never used to assign weights, score options, or influence the final ranking outcome.

- For benefit-type criteria, higher normalized values always represent better performance.

- For cost-type criteria, lower real-world values are transformed such that lower cost corresponds to higher utility during normalization.

- The system assumes that relative comparisons and trade-offs are more valuable to users than absolute precision. As a result, the model prioritizes consistency and explainability over perfect real-world accuracy.

## Why the Solution Is Structured This Way

| Problem / Constraint                           | Design Choice/ Solution                                                                                                   |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Users think in messy, unstructured ways   | **Free-form natural language input** is accepted and then progressively structured into discrete options and criteria using AI-assisted analysis, mirroring how humans naturally describe problems. |
| Users may not know all criteria upfront   | An **iterative, step-by-step confirmation flow** allows criteria to be added, removed, or modified at any stage, acknowledging that clarity often emerges during the decision-making process. |
| Not all criteria are numeric               | The system provides **robust support for both numeric and ordinal (qualitative) criteria**, allowing users to use descriptors like "Excellent" or "Poor" through user-defined or auto-generated mapping scales. |
| Users struggle with trade-offs | A **Weighted Multi-Criteria Decision Model (MCDM)** is used to make importance explicit. By forcing a relative ranking of criteria, the system quantifies trade-offs that are usually handled poorly by human intuition. |
| Black-box AI recommendations reduce trust | A **Deterministic Scoring Engine** ensures that rankings are 100% reproducible and auditable. The system prioritizes mathematical transparency over "black-box" AI-generated rankings. |
| AI can hallucinate or overstep | **Restricted AI Role:** AI is strictly confined to structuring messy input and explaining results. It is architecturally prohibited from assigning weights, scoring options, or influencing the final ranking. |
| Users may not know exact values | **Graceful Handling of Missing Data:** The system uses weight renormalization to handle missing values, providing explicit warnings rather than making silent, potentially incorrect assumptions. |
| Different criteria have different semantics | **Benefit vs. Cost Normalization:** The engine automatically handles "higher-is-better" (benefit) and "lower-is-better" (cost) logic, ensuring a consistent and mathematically sound interpretation across all dimensions. |
| Explanations often don’t match results | **Output-Driven Explanations:** The explanation payload is derived directly from the scoring engine's raw data, ensuring the natural language narrative is an honest reflection of the underlying math. |
| Users want to “see why” one option won | **Per-Option Factor Breakdown:** Every option is presented with its top positive and negative contributors, highlighting exactly which criteria drove its final rank. |
| Decision logic should work across domains | A **Domain-Agnostic Core** allows the same engine to be used for everything from choosing a car or a job to evaluating complex business software or travel destinations. |
| Criteria have different units (e.g., $ vs km) | **Min-Max Normalization** scales all raw values to a uniform 0.0–1.0 range, preventing criteria with large absolute numbers (like price) from unfairly dominating the final score. |
| Not all criteria are equally important | **Unique Importance Ranking:** Users provide a unique 1-N rank for each criterion, which is then mathematically converted into importance weights that sum to 1.0. |
| Qualitative descriptors are subjective | **User-Defined Ordinal Scales:** Users define the exact sequence of qualitative terms (e.g., "Good > Decent > Bad"), ensuring the system interprets descriptors according to the user's personal context. |

### Underlying Decision Model

The system is structured around a **Weighted Multi-Criteria Decision-Making (MCDM)** approach:

- **Multi-Criteria Evaluation:** Each option is evaluated against multiple, independent criteria.
- **Weighted Importance:** Each criterion is assigned an importance weight by the user.
- **Normalized Scoring:** Each option receives a normalized score (0 to 1) per criterion to ensure fair comparison across different units.
- **Weighted Sum Calculation:** Final scores are computed as a weighted sum, representing the overall utility of each option.

This approach was chosen because it is:
- **Simple and Well-Established:** Grounded in decision science.
- **Transparent and Explainable:** Every part of the score can be audited.
- **Flexible:** Works across any decision domain (cars, jobs, products, etc.).
- **User-Centric:** Easy for users to understand, inspect, and modify.

Most importantly, this structure ensures the system helps users **reason about trade-offs**, rather than hiding logic behind a black-box recommendation.

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
