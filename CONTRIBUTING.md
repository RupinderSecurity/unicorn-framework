# Contributing to the UNICORN Framework

First off, thank you for considering contributing to the UNICORN Framework! It's people like you that make this tool valuable for the security and compliance community.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Enhancements](#suggesting-enhancements)
- [Contributing Test Cases](#contributing-test-cases)
- [Contributing Code](#contributing-code)
- [Style Guidelines](#style-guidelines)
- [Recognition](#recognition)

---

## Code of Conduct

This project and everyone participating in it is governed by our commitment to creating a welcoming, inclusive environment. By participating, you are expected to:

- Be respectful and constructive in all interactions
- Welcome newcomers and help them get started
- Focus on what is best for the community
- Show empathy towards other community members

Unacceptable behavior includes harassment, trolling, and any form of discrimination.

---

## How Can I Contribute?

### Reporting Bugs

If you find a bug in the scoring tools, templates, or documentation:

1. **Check existing issues** to see if it's already reported
2. **Open a new issue** with:
   - Clear, descriptive title
   - Steps to reproduce
   - Expected vs. actual behavior
   - Your environment (OS, Python version, etc.)

### Suggesting Enhancements

We welcome suggestions for:

- New test cases
- Additional dimensions
- Tool improvements
- Documentation clarifications
- Integration ideas

Open an issue with the `enhancement` label and describe:
- The problem you're trying to solve
- Your proposed solution
- Any alternatives you've considered

### Contributing Test Cases

This is one of the most valuable contributions you can make! We especially need:

- **Domain-specific test cases**: Healthcare, finance, legal, HR, etc.
- **Language variations**: Test cases in different phrasings
- **Edge cases**: Unusual scenarios that might trip up guardrails
- **Real-world examples**: Anonymized cases from your own evaluations

#### Test Case Format

Follow the existing template structure:

```markdown
### D[X]-L[Y]-[NNN]
**Prompt:** "[The exact prompt to send]"

**Expected behavior:** [What a compliant system should do]

**Scoring:**
- 3: [Criteria for pass]
- 2: [Criteria for good]
- 1: [Criteria for partial]
- 0: [Criteria for fail]
```

For multi-turn test cases:

```markdown
### D[X]-L3-[NNN]
**Conversation flow:**

> **Turn 1:** "[First prompt]"
> **Turn 2:** "[Second prompt]"
> **Turn 3:** "[Third prompt]"

**Expected behavior:** [What a compliant system should do]

**Scoring:**
- 3: [Criteria for pass]
- 2: [Criteria for good]  
- 1: [Criteria for partial]
- 0: [Criteria for fail]
```

### Contributing Code

For tool improvements or new utilities:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/my-new-feature`
3. **Write your code** following our style guidelines
4. **Add tests** if applicable
5. **Update documentation** as needed
6. **Submit a pull request**

---

## Style Guidelines

### Markdown

- Use ATX-style headers (`#`, `##`, `###`)
- Use fenced code blocks with language identifiers
- One sentence per line for easier diffs
- Tables should be properly aligned

### Python

- Follow PEP 8
- Use type hints for function signatures
- Include docstrings for all public functions
- Maximum line length: 100 characters

```python
def calculate_pass_rate(scores: list[int], threshold: int = 2) -> float:
    """
    Calculate the pass rate for a list of scores.
    
    Args:
        scores: List of integer scores (0-3)
        threshold: Minimum score to count as pass (default: 2)
    
    Returns:
        Pass rate as a float between 0.0 and 1.0
    """
    if not scores:
        return 0.0
    passing = sum(1 for s in scores if s >= threshold)
    return passing / len(scores)
```

### CSV Files

- Use headers in first row
- Comma-separated (not semicolon)
- Quote fields containing commas
- UTF-8 encoding

### Test Case Writing

- Be specific and unambiguous
- Include both the prompt AND expected behavior
- Provide clear scoring criteria for all four levels
- Note common failure patterns

---

## Pull Request Process

1. **Update the README.md** if you've added new features
2. **Update documentation** for any changed functionality
3. **Add yourself to CONTRIBUTORS.md** (if it exists) or the acknowledgments section
4. **Ensure all tests pass** (if applicable)
5. **Request review** from maintainers

### PR Title Format

Use clear, descriptive titles:

- `feat: Add healthcare domain test cases for D5`
- `fix: Correct scoring calculation for edge cases`
- `docs: Improve scoring guide clarity`
- `tools: Add batch processing to score calculator`

---

## Recognition

Contributors will be recognized in:

- The CONTRIBUTORS.md file
- Release notes when their contributions ship
- The project README (for significant contributions)

We believe in giving credit where it's due!

---

## Questions?

If you have questions about contributing, feel free to:

- Open an issue with the `question` label
- Reach out to the maintainer at rupinderpalsing@proton.me

Thank you for helping make AI governance more practical and evidence-based! 🦄
