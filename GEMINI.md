# Decision-Lens Context

## Project Overview
**Decision-Lens** is a Decision Companion System designed to assist users in making informed decisions by evaluating multiple options against defined criteria using a weighted scoring model. The system prioritizes transparency and deterministic logic over black-box AI.

### Core Philosophy
- **Deterministic Logic:** Final rankings are produced using a weighted sum approach.
- **Explainability:** Users can audit exactly why an option ranks higher via a factual payload and AI-narrated explanations.
- **Human-in-the-Loop:** Users retain full control and can override AI suggestions or manual inputs at any stage.
- **Optional AI:** AI is strictly assistive (e.g., structuring messy input, narrating results) and never handles the core mathematical scoring.
- **Focus on User Intent:** The system is designed for users to express their intent and facts, while the system handles normalization and scoring.

### Key Technologies
- **Language:** Python 3.10+
- **External APIs:** OpenAI API (GPT-4o-mini) for structuring and explanation.
- **Libraries:** `python-dotenv` for environment management, `openai` for LLM interaction.

## Architecture & Data Structures
- `src/main.py`: Entry point. Orchestrates the interactive workflow, engine execution, and agent calls.
- `src/core/decision_engine.py`: Core scoring engine using weighted sum logic with min-max normalization.
- `src/core/explanation_builder.py`: Constructs a deterministic, factual audit payload from raw engine outputs.
- `src/core/attribute_mapper.py`: Converts raw descriptors into standardized numeric values based on user-confirmed ordinal scales.
- `src/agents/structure_agent.py`: Parses unstructured natural language input into a draft decision model (JSON).
- `src/agents/explanation_agent.py`: Transforms the factual explanation payload into a human-friendly narrative.
- `src/utils/input_helpers.py`: Contains complex CLI logic for confirming options, criteria, scales, and rankings.

### Data Schema
- `options`: `dict` mapping option names to attribute dictionaries.
- `criteria`: `dict` mapping criteria names to metadata (type, scale, unit, description).
- `weights`: `dict` mapping criteria to normalized importance weights (sum to 1.0).
- `mapped_attributes`: `dict[str, dict[str, float]]` (Stored with normalized underscore keys for engine processing).

## Documentation & Diagrams
- `README.md`: Comprehensive project guide, setup instructions, and design documentation.
- `BUILD_PROCESS.md`: Detailed log of the development lifecycle and key design shifts.
- `RESEARCH_LOG.md`: Archive of AI prompts, search queries, and technical exploration.
- `Dataflow.md`: Mermaid-based technical data flow overview.

## Building and Running

### Prerequisites
- Python 3.10+
- OpenAI API Key (stored in `.env` as `OPENAI_API_KEY`)

### Execution
```bash
python src/main.py
```

### Testing API Connectivity
```bash
python src/agents/test_openai_key.py
```

## Development Conventions
- **Functional Logic:** Core engine logic must remain pure and reproducible.
- **User Agency:** AI should only suggest; the user must always have a "confirm/edit" step for any AI-generated data.
- **Surgical Updates:** Documentation must be kept in sync with code changes, especially the architecture and data flow sections.

## Roadmap
- [x] Transition to dynamic CLI inputs.
- [x] Integrate AI-assisted input structuring (GPT-4o-mini).
- [x] Implement deterministic explanation payload builder.
- [x] Add AI-narrated natural language explanations.
- [x] Support for interactive post-result modifications (What-if analysis).
- [ ] Add a persistence layer (SQLite) to save and compare different decision sessions.
- [ ] Implement a comprehensive `pytest` test suite with mocked AI responses.
- [ ] Explore a web-based interface (React/FastAPI) for improved visualization.
