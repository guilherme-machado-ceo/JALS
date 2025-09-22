# Getting Started with JALS

Welcome to JALS (Journey Amplified Language Systems)! This guide will help you set up and start using JALS for linguistic amplification and multimodal language processing.

## What is JALS?

JALS is an innovative system for linguistic amplification through computational layers, designed to transform handwritten manuscripts into symbolic abstractions and multimodal linguistic integrations.

### Key Features

- 🖋️ **Manuscript Capture**: Capture and process handwritten gestures
- 🔄 **Symbolic Abstraction**: Transform writing into abstract symbols
- 🌐 **Language Integration**: Multimodal linguistic processing
- 🚀 **Computational Deployment**: Deploy across multiple platforms

## Prerequisites

Before starting, make sure you have:

- Python 3.9 or higher
- Git installed
- At least 4GB of available RAM
- Internet connection for downloading dependencies

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/guilherme-machado-ceo/JALS.git
cd JALS
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv jals_env

# Activate virtual environment
# On Windows:
jals_env\Scripts\activate
# On macOS/Linux:
source jals_env/bin/activate
```

### 3. Install Dependencies

```bash
# Update pip
pip install --upgrade pip

# Install JALS dependencies
pip install -r requirements.txt

# Install JALS in development mode
pip install -e .
```

### 4. Verify Installation

```bash
# Test the installation
python -c "import jals; print('JALS installed successfully!')"
```

## Quick Start

### Basic Usage Example

```python
from jals.core import CoreIdeogram, AmplificationEngine
from jals.layers import Layer1, Layer2, Layer3, Layer4

# Initialize core components
ideogram = CoreIdeogram()
engine = AmplificationEngine()

# Initialize processing layers
layer1 = Layer1()  # Manuscript Encoding
layer2 = Layer2()  # Symbolic Abstraction
layer3 = Layer3()  # Language Integration
layer4 = Layer4()  # Computational Deployment

# Process a manuscript sample
manuscript_data = layer1.capture("data/samples/manuscript_samples.json")
print(f"Captured {len(manuscript_data['strokes'])} strokes")

# Transform through layers
symbolic_data = layer2.abstract(manuscript_data)
language_data = layer3.integrate(symbolic_data)
result = layer4.deploy(language_data)

print("Processing complete!")
print(f"Result: {result}")
```

### Working with Sample Data

JALS comes with sample data to help you get started:

```python
import json
from jals.layers import Layer1

# Load sample manuscript data
with open("data/samples/manuscript_samples.json", "r") as f:
    sample_data = json.load(f)

# Initialize Layer 1
layer1 = Layer1()

# Process the sample
processed = layer1.preprocess(sample_data)
features = layer1.extract_features(processed)
encoded = layer1.encode(features)

print("Sample processing complete!")
```

## Understanding the Architecture

### The Four Layers

1. **Layer 1: Manuscript Encoding**
   - Captures handwritten gestures
   - Extracts geometric and kinematic features
   - Encodes data for further processing

2. **Layer 2: Symbolic Abstraction**
   - Transforms raw data into symbols
   - Identifies relationships and patterns
   - Builds hierarchical representations

3. **Layer 3: Language Integration**
   - Integrates linguistic knowledge
   - Applies grammar rules and semantics
   - Creates multimodal representations

4. **Layer 4: Computational Deployment**
   - Deploys to various platforms
   - Provides APIs and services
   - Enables real-time processing

### Core Components

- **Core Ideogram**: The fundamental unit of meaning
- **Amplification Engine**: Transforms and amplifies expressions

## Configuration

### Basic Configuration

Create a configuration file `config.yaml`:

```yaml
# JALS Configuration
core:
  ideogram:
    resolution: [1920, 1080]
    sampling_rate: 100
  
  amplification:
    max_iterations: 10
    threshold: 0.8

layers:
  layer1:
    preprocessing:
      noise_filter: true
      normalization: true
    
  layer2:
    symbol_recognition:
      confidence_threshold: 0.7
    
  layer3:
    language_models:
      default: "multilingual"
    
  layer4:
    deployment:
      platforms: ["web", "mobile"]
```

### Environment Variables

Set up environment variables for sensitive configurations:

```bash
# Database configuration
export JALS_DB_URL="postgresql://user:password@localhost/jals"

# API keys (if needed)
export JALS_API_KEY="your-api-key"

# Debug mode
export JALS_DEBUG=true
```

## Advanced Usage

### Custom Processing Pipeline

```python
from jals.core import CoreIdeogram
from jals.layers import Layer1, Layer2

# Create custom pipeline
class CustomPipeline:
    def __init__(self):
        self.layer1 = Layer1()
        self.layer2 = Layer2()
        
    def process(self, data):
        # Custom preprocessing
        preprocessed = self.custom_preprocess(data)
        
        # Standard layer processing
        encoded = self.layer1.encode(preprocessed)
        abstracted = self.layer2.abstract(encoded)
        
        return abstracted
    
    def custom_preprocess(self, data):
        # Your custom preprocessing logic
        return data

# Use custom pipeline
pipeline = CustomPipeline()
result = pipeline.process(manuscript_data)
```

### Batch Processing

```python
import os
from jals.utils import batch_processor

# Process multiple files
input_dir = "data/manuscripts/"
output_dir = "data/processed/"

# Batch process all files in directory
results = batch_processor.process_directory(
    input_dir=input_dir,
    output_dir=output_dir,
    layers=[Layer1(), Layer2(), Layer3()]
)

print(f"Processed {len(results)} files")
```

## Testing Your Setup

### Run Unit Tests

```bash
# Run all tests
pytest

# Run specific test module
pytest tests/test_core.py

# Run with coverage
pytest --cov=src tests/
```

### Validate Sample Processing

```python
from jals.validation import validate_setup

# Run validation checks
validation_results = validate_setup()

if validation_results["success"]:
    print("✅ JALS setup is valid!")
else:
    print("❌ Setup issues found:")
    for issue in validation_results["issues"]:
        print(f"  - {issue}")
```

## Next Steps

Now that you have JALS set up, you can:

1. **Explore Examples**: Check the `examples/` directory for more use cases
2. **Read Documentation**: Dive deeper into the [Architecture Documentation](../architecture/README.md)
3. **Join Community**: Participate in [GitHub Discussions](https://github.com/guilherme-machado-ceo/JALS/discussions)
4. **Experiment**: Try processing your own handwritten samples
5. **Contribute**: Read the [Contributing Guide](../../CONTRIBUTING_EN.md) to contribute to the project

## Troubleshooting

### Import Errors

If you receive import errors:

```bash
# Make sure the package is installed in development mode
pip install -e .
```

### Dependency Issues

```bash
# Update pip
pip install --upgrade pip

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Sample Data Not Found

```bash
# Make sure you're in the project root directory
ls data/samples/manuscript_samples.json
```

## Support

- **Issues**: [GitHub Issues](https://github.com/guilherme-machado-ceo/JALS/issues)
- **Discussions**: [GitHub Discussions](https://github.com/guilherme-machado-ceo/JALS/discussions)
- **Email**: guilherme.ceo@hubstry.com

## License

This project is licensed under the MIT License. See the [LICENSE](../../LICENSE) file for details.

---

**Congratulations!** 🎉 You now have JALS running in your environment. Explore, experiment, and contribute to the future of linguistic amplification!

---

**🌐 Language Versions:**
- [Português (Portuguese)](getting_started.md) - Original version
- [English](getting_started_EN.md) - This version