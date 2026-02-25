def normalize_text(value: str) -> str:
    return value.strip().lower()


def map_attributes(structured_data: dict) -> dict:
    """
    Converts structure-agent output into engine-ready numeric attributes.
    Supports both numeric values and ordinal descriptors.
    """

    criteria = structured_data.get("criteria", {})
    options = structured_data.get("options", {})

    mapped = {}

    for option, attrs in options.items():
        mapped[option] = {}

        for criterion, raw_value in attrs.items():
            c_key = normalize_text(criterion.replace("_", " "))

            # Unknown stays unknown
            if raw_value == "unknown":
                mapped[option][criterion] = None
                continue

            # Numeric values pass through directly
            if isinstance(raw_value, (int, float)):
                mapped[option][criterion] = raw_value
                continue

            # Ordinal descriptor handling
            scale = criteria.get(c_key, {}).get("scale")

            if not scale:
                mapped[option][criterion] = None
                continue

            scale_normalized = [normalize_text(s) for s in scale]
            value_key = normalize_text(str(raw_value))

            if value_key not in scale_normalized:
                mapped[option][criterion] = None
                continue

            # Ordinal rank (1-based)
            mapped[option][criterion] = scale_normalized.index(value_key) + 1

    return mapped