
import pytest
from calculator import add, subtract, multiply

# Tests for add function
def test_add_positive_numbers() -> None:
    assert add(1, 2) == 3

def test_add_negative_numbers() -> None:
    assert add(-1, -2) == -3

def test_add_positive_and_negative_numbers() -> None:
    assert add(5, -3) == 2

def test_add_zero() -> None:
    assert add(5, 0) == 5

def test_add_floats() -> None:
    assert add(0.1, 0.2) == pytest.approx(0.3)

def test_add_large_numbers() -> None:
    assert add(1_000_000_000, 2_000_000_000) == 3_000_000_000

@pytest.mark.parametrize("a, b", [(1, "2"), ("1", 2), (None, 2), (1, None)])
def test_add_invalid_input(a, b) -> None:
    with pytest.raises(TypeError):
        add(a, b)

# Tests for subtract function
def test_subtract_positive_numbers() -> None:
    assert subtract(3, 1) == 2

def test_subtract_negative_numbers() -> None:
    assert subtract(-1, -2) == 1

def test_subtract_positive_and_negative_numbers() -> None:
    assert subtract(5, -3) == 8

def test_subtract_from_zero() -> None:
    assert subtract(0, 5) == -5

def test_subtract_floats() -> None:
    assert subtract(0.3, 0.1) == pytest.approx(0.2)

def test_subtract_large_numbers() -> None:
    assert subtract(3_000_000_000, 1_000_000_000) == 2_000_000_000

@pytest.mark.parametrize("a, b", [(1, "2"), ("1", 2), (None, 2), (1, None)])
def test_subtract_invalid_input(a, b) -> None:
    with pytest.raises(TypeError):
        subtract(a, b)

# Tests for multiply function
def test_multiply_positive_numbers() -> None:
    """Test that the multiply function correctly multiplies two positive numbers."""
    assert multiply(2, 3) == 6

def test_multiply_negative_numbers() -> None:
    """Test that the multiply function correctly multiplies two negative numbers."""
    assert multiply(-2, -3) == 6

def test_multiply_positive_and_negative_numbers() -> None:
    """Test that the multiply function correctly multiplies a positive and a negative number."""
    assert multiply(2, -3) == -6

def test_multiply_by_zero() -> None:
    """Test that the multiply function correctly multiplies by zero."""
    assert multiply(5, 0) == 0

def test_multiply_by_one() -> None:
    """Test that the multiply function correctly multiplies by one."""
    assert multiply(5, 1) == 5

def test_multiply_floats() -> None:
    """Test that the multiply function correctly multiplies two floating-point numbers."""
    assert multiply(0.5, 0.5) == pytest.approx(0.25)

def test_multiply_large_numbers() -> None:
    """Test that the multiply function correctly multiplies two large numbers."""
    assert multiply(1_000_000, 2_000_000) == 2_000_000_000_000

@pytest.mark.parametrize("a, b", [(1, "2"), ("1", 2), (None, 2), (1, None)])
def test_multiply_invalid_input(a, b) -> None:
    """Test that the multiply function raises a TypeError for invalid input."""
    with pytest.raises(TypeError):
        multiply(a, b)
