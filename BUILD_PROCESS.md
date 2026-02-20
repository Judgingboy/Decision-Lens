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
After validating the core engine, the focus shifted to interactive user engagement.

### Key Implementations:
- **Interactive Input:** Developed `src/utils/input_helpers.py` to handle iterative CLI input for options and criteria.
- **Dynamic Weighting:** Implemented a system where users enter raw importance values for each criterion, which the system automatically normalizes to sum to 1.
- **Validation Layer:** Integrated robust checks in `src/core/validation.py` to ensure all options are rated across all criteria before computation.

## Current State
The system is now a fully functional, dynamic CLI-based Decision Companion System. 
- **Modular Architecture:** The codebase is partitioned into `core` (engine/validation) and `utils` (UI/input).
- **Transparency:** Every ranking is auditable and based directly on user-provided scores and weights.
- **Human-in-the-Loop:** Users retain full control over the inputs, with the system acting as a supportive analytical tool.

## Future Roadmap
- **AI-Assisted Gathering:** Integrating LLMs to suggest criteria or options when users are "stuck."
- **Persistence:** Adding the ability to save, export, and revisit past decision matrices.
- **Enhanced Visualization:** Implementing graphical score breakdowns and trade-off visualizations.
- **Testing Suite:** Expanding the inline assertions into a comprehensive `pytest` suite.
