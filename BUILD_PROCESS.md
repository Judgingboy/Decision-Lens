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

### Key Implementations
- **Interactive Input Layer:** Created `src/utils/input_helpers.py` to collect options and criteria dynamically.
- **Dynamic Weighting:** Allowed users to express importance, which the system normalized so that weights always sum to 1.
- **Validation Layer:** Added checks in `src/core/validation.py` to ensure completeness and consistency of inputs.

At this stage, the system became fully dynamic and runnable end-to-end.

## Phase 4: Critical Usability & Model Flaw Discovery

During real-world testing and iterative use, the system exposed fundamental modeling and usability flaws. These issues were not implementation bugs but structural problems in how decisions were being represented and evaluated.

### Cost vs Benefit Criteria Misinterpretation

The initial scoring logic implicitly treated all criteria as “higher is better.”

- This caused incorrect behavior for cost-based criteria (e.g., price, time, effort), where lower values should be preferred.
- Although criteria were labeled as cost or benefit at input time, this distinction was not properly integrated into normalization and scoring logic.
- As a result, the model could produce rankings that directly contradicted user intent.

This revealed that correct handling of cost vs benefit is not a UX concern but a core mathematical requirement of any decision model.

### User Cognitive Overload & Input Model Breakdown

The original interaction model required users to:
- Rank criteria by importance.
- Manually rate every option on a 1–10 scale for every criterion.

Testing showed this dual-input requirement to be unintuitive, error-prone, and cognitively unrealistic for most users.

Users consistently struggled to:
- Translate real-world facts into abstract numeric ratings.
- Understand how ratings interacted with priority weights.
- Predict or trust the resulting rankings.

Even when user intent was clear, outcomes often felt confusing or counterintuitive.
This demonstrated that the problem was not user error, but a flawed assumption that humans can reliably perform normalization and scoring tasks.

## Phase 5: Revised Model — AI-Assisted Structuring (Current Direction)

> Users should express intent and facts, not perform scoring or normalization.

### Revised Architecture

The system is now divided into three clearly defined layers:

1.  **Structure Agent (AI-Assisted)**
    - Converts natural language input into structured data.
    - **Extracts:**
        - Options
        - Criteria
        - Cost vs benefit classification
        - Option attributes (numeric or descriptive)
    - **Emits** ordinal scales for descriptive criteria.
    - **Marks** missing information explicitly.
    - **Does not:**
        - Score, rank, or assign weights.

2.  **Core Decision Engine (Deterministic)**
    - Converts ordinal descriptors to numeric values.
    - Accepts raw numeric attributes directly.
    - Normalizes values across options.
    - Applies user-defined criterion weights.
    - Correctly handles cost vs benefit criteria.
    - Produces ranked results.
    - No AI is used in this layer.

3.  **Explanation Agent (Optional AI)**
    - Explains rankings using engine outputs.
    - Highlights trade-offs based on user priorities.
    - **Does not** recalculate or override results.

### Attribute Model

The system supports:
-   Numeric attributes (e.g., price, calories, protein)
-   Ordinal attributes (e.g., cheap → expensive, low → high)

Ordinal scales are explicit and decision-specific.

### Missing-Data Policy

If an option lacks data for a criterion:
-   That criterion is excluded for the option.
-   Remaining weights are re-normalized.

This avoids penalizing uncertainty or encouraging guesses.

### Outcome

The revised model:
-   Removes arbitrary 1–10 ratings
-   Reduces user effort
-   Remains fully explainable and deterministic
-   Works across multiple decision domains

### Key Insight
> Users should express intent and factual information — not perform normalization, inversion, or scoring themselves. Normalization and trade-off math are system responsibilities, not human ones.

### Revised Interaction Model

**Users now:**
-   Define decision options.
-   Define evaluation criteria.
-   Rank criteria by importance.
-   Describe option attributes using natural language or factual terms.

**The system now:**
-   Explicitly classifies criteria as cost or benefit.
-   Normalizes attributes across options in a scale-independent manner.
-   Applies user-defined weights deterministically.
-   Produces a ranked outcome based on transparent calculations.

This preserves user control over priorities while removing unnecessary cognitive burden.

### Role of AI in the Revised Model

AI is introduced only as an assistive structuring layer, not as a decision-maker.

**AI is used to:**
-   Interpret vague or unstructured user descriptions.
-   Convert natural language into structured, comparable attributes.
-   Assist users when they are unsure how to define options or criteria.

**AI explicitly does not:**
-   Assign weights.
-   Rank options.
-   Override user priorities.
-   Make final decisions.

All decision logic remains deterministic and auditable.

### Current State of the System

The system is now a functional, CLI-based Decision Companion System with a clear separation of responsibilities.

#### Core Characteristics
-   **Core Engine:** Deterministic, explainable weighted scoring model.
-   **Normalization:** Proper handling of cost (lower is better) and benefit (higher is better) criteria.
-   **Architecture:** Modular separation between:
    -   `core` — decision engine and validation logic
    -   `utils` — user input and interaction helpers
-   **Decision Control:** User-defined priorities with system-managed normalization.
-   **AI Role:** Assistive interpretation only; no black-box decision-making.

#### Recent Technical Updates
-   Implemented normalization logic that correctly distinguishes between cost and benefit criteria.
-   Removed reliance on fixed rating-scale inversion.
-   Improved mathematical validity and interpretability of trade-offs.
-   Maintained full transparency: every score can be traced back to user inputs and deterministic rules.
-   Preserved a human-in-the-loop workflow where users retain full control over intent and priorities.

### Future Roadmap
-   **AI-Assisted Structuring:** Integrate LLMs to suggest criteria or options when users are uncertain or “stuck.”
-   **Persistence:** Enable saving, exporting, and revisiting past decision analyses.
-   **Visualization:** Add graphical breakdowns of scores and trade-offs for deeper insight.
-   **Testing:** Expand inline validation into a comprehensive `pytest` test suite.
