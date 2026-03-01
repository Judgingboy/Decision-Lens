# Data Flow Diagram

The following diagram illustrates the flow of data through the Decision-Lens system, from initial user input to the final generated explanation.

```mermaid
graph TD
    User([User]) -- "Natural Language Description" --> Main[src/main.py]
    
    Main -- "User Input" --> StructAgent[src/agents/structure_agent.py]
    StructAgent -- "Draft JSON (Options & Criteria)" --> Main
    
    Main -- "Draft Data" --> InputHelpers[src/utils/input_helpers.py]
    InputHelpers -- "User Interaction (Confirmation/Edits)" --> Main
    
    Main -- "Refined Data (Options & Criteria Meta)" --> AttrMapper[src/core/attribute_mapper.py]
    AttrMapper -- "Numeric Mapped Attributes" --> Main
    
    Main -- "Mapped Attributes + User Weights" --> Engine[src/core/decision_engine.py]
    Engine -- "Ranked Results + Normalized Values" --> Main
    
    Main -- "Results + Normalized Data + Weights" --> ExplBuilder[src/core/explanation_builder.py]
    ExplBuilder -- "Explanation Payload (JSON)" --> Main
    
    Main -- "Explanation Payload" --> ExplAgent[src/agents/explanation_agent.py]
    ExplAgent -- "Natural Language Explanation" --> Main
    
    Main -- "Final Ranking & Explanation" --> User
```

## Flow Description

1.  **Input & Structuring**: The user provides a natural language description of their decision problem. The `structure_agent` (using GPT-4o-mini) extracts a draft structure consisting of options and criteria.
2.  **Refinement**: `input_helpers` facilitate a series of user confirmation steps (confirming options, criteria, cost/benefit types, and ordinal scales).
3.  **Mapping**: The `attribute_mapper` converts qualitative descriptors (e.g., "high", "good") and numeric strings into a standardized numeric format based on the defined scales and units.
4.  **Scoring**: The `decision_engine` applies a weighted sum model to the mapped attributes. It handles missing values through weight renormalization and normalizes scores across options.
5.  **Payload Building**: The `explanation_builder` constructs a deterministic JSON payload that identifies top positive/negative factors and missing data for each option.
6.  **Explanation**: The `explanation_agent` transforms the factual payload into a human-readable, natural language explanation for the user.


