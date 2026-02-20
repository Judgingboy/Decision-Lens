# Decision-Lens Context

## Project Overview
**Decision-Lens** is a Decision Companion System designed to assist users in making informed decisions by evaluating multiple options against defined criteria using a weighted scoring model. The system prioritizes transparency and deterministic logic over black-box AI.

### Core Philosophy
- **Deterministic Logic:** Final rankings are produced using a weighted sum approach.
- **Explainability:** Users can audit exactly why an option ranks higher.
- **Human-in-the-Loop:** Users retain full control and can override inputs at any stage.
- **Optional AI:** AI is strictly assistive (e.g., suggesting criteria/options) and does not handle the core scoring.

### Key Technologies
- **Language:** Python 3 (standard library)
- **Architecture:** Modular Python package with a clear separation between the entry point (`src/main.py`) and core logic (`src/core/`).

## Architecture & Data Structures
- `src/main.py`: Entry point. Orchestrates dynamic user input and core engine.
- `src/core/decision_engine.py`: Implements `compute_weighted_scores`.
- `src/core/validation.py`: Handles input validation.
- `src/utils/input_helpers.py`: Provides helper functions for interactive CLI input gathering.

### Data Schema
- `options`: `list[str]`
- `criteria`: `list[str]`
- `weights`: `dict[str, float]` (Maps criterion to importance weight)
- `ratings`: `dict[str, dict[str, float]]` (Maps option to a dictionary of criterion scores)

## Building and Running

### Execution
Run the interactive CLI:
```bash
python src/main.py
```

### Testing
- Currently uses inline `assert` statements.
- TODO: Implement `pytest` for comprehensive coverage.

## Development Conventions
- **Functional Logic:** Core logic should remain pure and deterministic.
- **Validation:** Always use `validate_weights` and `validate_ratings` before processing data.
- **No External Dependencies:** Keep the core system lightweight using Python's standard library unless explicitly required.

## Roadmap
- [x] Transition to dynamic CLI inputs.
- [ ] Integrate AI-assisted input gathering (criteria/option suggestions).
- [ ] Add visualization for score breakdowns.
- [ ] Add `pytest` test suite.
