# Build Process

## Phase 1: Initial Understanding & Static Prototype
The goal was to build a Decision Companion System (DCS) that assists users in making better decisions by structuring trade-offs explicitly. The system was designed to prioritize deterministic logic over black-box AI recommendations to ensure transparency and trust.

### Approach:
- Defined the core data structures: options, criteria, weights, and ratings.
- Implemented the `compute_weighted_scores` engine using standard Python.
- Validated the logic using a static, hardcoded model in `main.py` to ensure mathematical accuracy before building the user interface.

## Phase 2: Design Evolution & Refinement
Initially, a chatbot-style interface was considered. However, this was rejected to avoid obscuring the decision logic and over-relying on AI. The design was refined to:
- Use deterministic weighted scoring as the core decision engine.
- Position AI strictly as an optional assistive layer.
- Ensure the system remains functional even if AI components are unavailable.

## Phase 3: Transition to Dynamic CLI
After validating the core engine, the focus shifted toward building a dynamic CLI-based system that allows real user input.

Key Implementations
Interactive Input Layer: Created src/utils/input_helpers.py to collect options and criteria dynamically.
Dynamic Weighting: Allowed users to express importance, which the system normalized so that weights always sum to 1.
Validation Layer: Added checks in src/core/validation.py to ensure completeness and consistency of inputs.
At this stage, the system became fully dynamic and runnable end-to-end.

## Phase 4: Critical Usability & Model Flaw Discovery
During real-world testing, two major issues were identified:

### Cost vs Benefit Criteria Problem
- The system treated all criteria as if “higher values are better.”
- This caused incorrect behavior for cost-based criteria (e.g., price), where lower values should be preferred.
- Although criteria were labeled as cost or benefit, this information was not yet used in normalization and scoring.

### User Cognitive Overload
The system required users to:
1. Rank criteria by importance.
2. Manually rate each option on a 1–10 scale for every criterion.

Testing revealed that this dual input model was unintuitive, error-prone, and unrealistic for average users. Users struggled to:
- Translate real-world facts into abstract scores.
- Understand how ratings interacted with priorities.
- Predict or trust the resulting rankings.

This led to confusing and counterintuitive outcomes, even when user intent was clear. These issues were not simple bugs but fundamental modeling and UX flaws.

## Phase 5: Revised Model – AI-Assisted Structuring (Current Direction)
To resolve these issues, the system design was revised.

### Key Insight
**Users should express intent and facts, not perform normalization or scoring themselves.**

### Revised Approach
**Users:**
- Define options.
- Define criteria.
- Rank criteria by importance.
- Describe option attributes in natural language or factual terms.

**The System:**
- Classifies criteria as cost or benefit.
- Normalizes numeric and categorical attributes.
- Applies weights deterministically.
- Produces a ranked outcome.

### Role of AI
AI is introduced only to:
- Interpret unstructured or vague user descriptions.
- Convert them into structured, comparable attributes.
- Assist users when they are unsure how to describe options or criteria.

AI does **not**:
- Apply weights.
- Rank options.
- Make final decisions.

This preserves explainability while significantly improving usability and correctness.

## Current State
The system is now a fully functional, dynamic CLI-based Decision Companion System.
- Core Engine: Deterministic, explainable weighted scoring
- Architecture: Modular separation between core logic and input/assistance layers
- Decision Control: Fully user-driven priorities with system-managed normalization
- AI Role: Assistive interpretation, not decision-making

- **Recent Update:** Logic added to distinguish between "Benefit" (higher is better) and "Cost" (lower is better) criteria.
- **Modular Architecture:** The codebase is partitioned into `core` (engine/validation) and `utils` (UI/input).
- **Transparency:** Every ranking is auditable and based directly on user-provided scores and weights.
- **Human-in-the-Loop:** Users retain full control over the inputs, with the system acting as a supportive analytical tool.

## Future Roadmap
- **AI-Assisted Gathering:** Integrating LLMs to suggest criteria or options when users are "stuck."
- **Persistence:** Adding the ability to save, export, and revisit past decision matrices.
- **Enhanced Visualization:** Implementing graphical score breakdowns and trade-off visualizations.
- **Testing Suite:** Expanding the inline assertions into a comprehensive `pytest` suite.
