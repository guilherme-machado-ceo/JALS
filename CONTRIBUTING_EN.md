# Contributing to JALS

Thank you for your interest in contributing to JALS! This document provides guidelines and information for contributors.

## 🌟 How to Contribute

There are many ways to contribute to JALS:

- **Code**: Implement new features, fix bugs, improve performance
- **Documentation**: Write tutorials, improve existing docs, translate content
- **Testing**: Write tests, report bugs, test new features
- **Design**: Create interfaces, improve UX, design graphics
- **Community**: Help other users, participate in discussions

## 🚀 Getting Started

### 1. Fork and Clone

```bash
# Fork the repository on GitHub
# Then clone your fork
git clone https://github.com/YOUR_USERNAME/JALS.git
cd JALS

# Add the original repository as upstream
git remote add upstream https://github.com/guilherme-machado-ceo/JALS.git

# Keep your main branch updated
git checkout main
git pull upstream main

# Create a new branch for your contribution
git checkout -b feature/feature-name
# or
git checkout -b bugfix/bug-name
# or
git checkout -b docs/documentation-improvement
```

### 2. Make Your Changes

- Follow the [code guidelines](#code-guidelines)
- Add tests for new features
- Update documentation as needed
- Keep commits small and focused

### 3. Test Your Changes

```bash
# Run tests
pytest

# Check code style
flake8 src tests

# Format code
black src tests
```

### 4. Commit and Push

```bash
# Add your changes
git add .

# Commit with descriptive message
git commit -m "feat: add functionality X for Layer 2"

# Push to your fork
git push origin feature/feature-name
```

### 5. Open a Pull Request

1. Go to the repository on GitHub
2. Click "New Pull Request"
3. Select your branch
4. Fill out the PR template
5. Wait for review

## 📝 Code Guidelines

### Code Style

- **Python**: We follow PEP 8
- **Formatting**: We use `black` for automatic formatting
- **Linting**: We use `flake8` for style checking
- **Docstrings**: We use Google/NumPy format

### Docstring Example

```python
def extract_features(self, data: Dict) -> Dict:
    """Extract features from manuscript data.
    
    This method processes raw manuscript data and extracts
    geometric and kinematic features for further analysis.
    
    Args:
        data (Dict): Raw manuscript data containing strokes
        
    Returns:
        Dict: Extracted features with geometric and kinematic data
        
    Raises:
        ValueError: If data format is invalid
        
    Example:
        >>> extractor = FeatureExtractor()
        >>> features = extractor.extract_features(manuscript_data)
        >>> print(features.keys())
        ['geometric', 'kinematic']
    """
    # Implementation here
    pass
```

### Testing Guidelines

Write comprehensive tests for all new code:

```python
import pytest
from src.core import CoreIdeogram

class TestCoreIdeogram:
    """Tests for Core Ideogram."""
    
    def setup_method(self):
        """Setup executed before each test."""
        self.ideogram = CoreIdeogram()
        
    def test_initialization(self):
        """Test correct initialization."""
        assert self.ideogram.data is not None
        assert 'strokes' in self.ideogram.data
        
    def test_feature_extraction(self):
        """Test feature extraction."""
        # Arrange
        test_data = {'strokes': [{'id': 1, 'points': [[0, 0], [1, 1]]}]}
        self.ideogram.data = test_data
        
        # Act
        features = self.ideogram.extract_features()
        
        # Assert
        assert 'geometric' in features
        assert 'kinematic' in features
```

### Test Coverage

- Maintain coverage > 80%
- Test success and failure cases
- Include integration tests
- Test edge cases

## 📚 Documentation

### Documentation Types

1. **Docstrings**: For functions and classes
2. **README**: Overview and basic instructions
3. **Tutorials**: Step-by-step guides
4. **API Reference**: Detailed technical documentation
5. **Whitepaper**: Theoretical foundation

### Updating Documentation

- Keep documentation synchronized with code
- Use practical examples
- Include diagrams when appropriate
- Translate to Portuguese when possible

## 🐛 Reporting Bugs

Use the bug issue template:

1. **Clear description** of the problem
2. **Steps to reproduce**
3. **Expected vs actual behavior**
4. **Environment** (OS, Python version, etc.)
5. **Error logs** if available

## 💡 Suggesting Features

Use the feature request template:

1. **Problem** the feature solves
2. **Proposed solution**
3. **Alternatives considered**
4. **Additional context**

## 🏷️ Commit Conventions

We use [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>[optional scope]: <description>

[optional body]

[optional footer]
```

### Commit Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Formatting, no code change
- `refactor`: Code refactoring
- `test`: Adding or fixing tests
- `chore`: Maintenance tasks

### Examples

```bash
feat(layer2): add advanced symbolic abstraction
fix(core): fix bug in feature extraction
docs(readme): update installation instructions
test(layer1): add tests for data capture
```

## 🔄 Review Process

### For Reviewers

- Be constructive and respectful
- Focus on code quality and design
- Test changes locally
- Check documentation and tests

### For Contributors

- Respond to comments promptly
- Make requested changes
- Keep discussions focused on code
- Be patient during the process

## 🏆 Recognition

Contributors are recognized through:

- **README**: Contributors list
- **Releases**: Mention in release notes
- **Documentation**: Credits on relevant pages

## 📞 Getting Help

- **Issues**: For bugs and features
- **Discussions**: For general questions
- **Email**: guilherme.ceo@hubstry.com

## 📄 Code of Conduct

This project adheres to the [Contributor Covenant](https://www.contributor-covenant.org/). By participating, you agree to maintain a respectful and inclusive environment.

### Our Commitments

- **Respect**: We treat everyone with dignity
- **Inclusion**: We value diversity of perspectives
- **Collaboration**: We work together constructively
- **Learning**: We support mutual growth

## 🎯 Contribution Roadmap

### Current Priorities

1. **Layers 2-4 Implementation**: Complete basic functionalities
2. **Testing**: Increase coverage to >90%
3. **Documentation**: Create tutorials and examples
4. **Performance**: Optimize data processing
5. **Interface**: Develop web/desktop interface

### Areas That Need Help

- 🧠 **ML Algorithms**: Model implementation
- 📊 **Visualization**: Dashboards and charts
- 🌐 **Internationalization**: Multi-language support
- 🔧 **DevOps**: CI/CD and deployment
- 📱 **Mobile**: Mobile applications

## 🙏 Acknowledgments

Thank you for contributing to JALS! Your participation helps build a future where human language is amplified and celebrated through technology.

---

**Remember**: Every contribution, no matter how small, is valuable. From typo fixes to complex feature implementations, everything helps make JALS better!

*Happy coding!* 🚀

---

**🌐 Language Versions:**
- [Português (Portuguese)](CONTRIBUTING.md) - Original version
- [English](CONTRIBUTING_EN.md) - This version