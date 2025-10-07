
def add(a: int | float, b: int | float) -> int | float:
    """Adds two numbers together."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a + b
