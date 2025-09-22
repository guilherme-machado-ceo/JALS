# JALS Data Directory

This directory contains sample data and datasets for the JALS project.

## Structure

- `samples/` - Sample data for testing and demonstrations
  - `manuscript_samples.json` - Examples of captured manuscript data
  - `symbolic_samples.json` - Examples of symbolic representations

## Data Format

### Manuscript Data
Manuscript data follows the format:
```json
{
  "metadata": {
    "source": "data_source",
    "resolution": [width, height],
    "sampling_rate": sampling_rate,
    "timestamp": "iso_timestamp",
    "user_id": "user_identifier"
  },
  "strokes": [
    {
      "id": stroke_identifier,
      "points": [[x1, y1], [x2, y2], ...],
      "timestamps": [t1, t2, ...],
      "pressure": [p1, p2, ...],
      "velocity": [v1, v2, ...]
    }
  ]
}
```

### Symbolic Data
Symbolic representations follow the format:
```json
{
  "symbols": [
    {
      "id": symbol_identifier,
      "type": "symbol_type",
      "properties": {
        "specific_properties": "values"
      }
    }
  ],
  "relationships": [
    {
      "source": "source_symbol_id",
      "target": "target_symbol_id",
      "type": "relationship_type",
      "strength": strength_value
    }
  ]
}
```

## Usage

To load sample data:

```python
from jals.layers import Layer1
import json

# Load manuscript data
layer1 = Layer1()
data = layer1.capture('data/samples/manuscript_samples.json')

# Process data
processed = layer1.preprocess(data)
features = layer1.extract_features(processed)
encoded = layer1.encode(features)
```

---

**🌐 Language Versions:**
- [Português (Portuguese)](README.md) - Original version
- [English](README_EN.md) - This version