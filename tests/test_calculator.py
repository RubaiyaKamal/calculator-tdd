
import pytest
from calculator import add

def test_add_positive_numbers() -> None:
    """Test that the add function correctly adds two positive numbers."""
    assert add(1, 2) == 3

def test_add_negative_numbers() -> None:
    """Test that the add function correctly adds two negative numbers."""
    assert add(-1, -2) == -3

def test_add_positive_and_negative_numbers() -> None:
    """Test that the add function correctly adds a positive and a negative number."""
    assert add(5, -3) == 2

def test_add_zero() -> None:
    """Test that the add function correctly adds zero to a number."""
    assert add(5, 0) == 5

def test_add_floats() -> None:
    """Test that the add function correctly adds two floating-point numbers."""
    assert add(0.1, 0.2) == pytest.approx(0.3)

def test_add_large_numbers() -> None:
    """Test that the add function correctly adds two large numbers."""
    assert add(1_000_000_000, 2_000_000_000) == 3_000_000_000

@pytest.mark.parametrize("a, b", [
    (1, "2"),
    ("1", 2),
    (None, 2),
    (1, None),
])
def test_add_invalid_input(a, b) -> None:
    """Test that the add function raises a TypeError for invalid input."""
    with pytest.raises(TypeError):
        add(a, b)
