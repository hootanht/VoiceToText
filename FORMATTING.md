# Code Formatting Guide

## Black Code Formatter

This project uses [Black](https://black.readthedocs.io/) for consistent Python code formatting.

### Local Development

Before committing code, ensure it's properly formatted:

```bash
# Install Black
pip install black

# Format all files
black .

# Check formatting without making changes
black --check .
```

### Formatting Standards

- **Line Length**: 88 characters (Black default)
- **Quotes**: Double quotes for strings
- **Indentation**: 4 spaces
- **Import Organization**: Standard library, third-party, local imports

### CI/CD Integration

The GitHub Actions workflow automatically checks code formatting. All Python files must pass Black formatting checks for the CI to succeed.

### Manual Formatting

If you need to fix formatting issues:

1. **Install Black locally**:
   ```bash
   pip install black
   ```

2. **Format your code**:
   ```bash
   black .
   ```

3. **Verify formatting**:
   ```bash
   black --check .
   ```

4. **Commit and push**:
   ```bash
   git add .
   git commit -m "Fix: Code formatting with Black"
   git push
   ```

### Example

Before Black formatting:
```python
def example_function( param1,param2 ):
    result='value1' if param1 else 'value2'
    return result
```

After Black formatting:
```python
def example_function(param1, param2):
    result = "value1" if param1 else "value2"
    return result
```

## Pre-commit Hooks (Optional)

For teams wanting to enforce formatting automatically, you can set up pre-commit hooks:

```bash
pip install pre-commit
pre-commit install
```

Note: Pre-commit may require additional setup depending on your development environment. 