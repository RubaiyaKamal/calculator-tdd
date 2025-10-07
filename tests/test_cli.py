
import pytest
import subprocess
import sys

# Define the path to the CLI script
CLI_PATH = [sys.executable, "-m", "calculator.__main__"]

def run_cli(args: list[str]) -> tuple[int, str, str]:
    """Helper function to run the CLI and capture its output."""
    result = subprocess.run(
        CLI_PATH + args,
        capture_output=True,
        text=True,
        check=False
    )
    return result.returncode, result.stdout.strip(), result.stderr.strip()

# --- Positive Test Cases ---

def test_cli_add_integers() -> None:
    """Test CLI addition with positive integers."""
    returncode, stdout, stderr = run_cli(["add", "10", "20"])
    assert returncode == 0
    assert stdout == "30.0"
    assert stderr == ""

def test_cli_subtract_floats() -> None:
    """Test CLI subtraction with floating-point numbers."""
    returncode, stdout, stderr = run_cli(["subtract", "10.5", "3.2"])
    assert returncode == 0
    assert pytest.approx(float(stdout)) == 7.3
    assert stderr == ""

def test_cli_multiply_negative_numbers() -> None:
    """Test CLI multiplication with negative numbers."""
    returncode, stdout, stderr = run_cli(["multiply", "-5", "-4"])
    assert returncode == 0
    assert stdout == "20.0"
    assert stderr == ""

def test_cli_divide_positive_numbers() -> None:
    """Test CLI division with positive integers."""
    returncode, stdout, stderr = run_cli(["divide", "10", "2"])
    assert returncode == 0
    assert stdout == "5.0"
    assert stderr == ""

def test_cli_divide_floats() -> None:
    """Test CLI division with floating-point numbers."""
    returncode, stdout, stderr = run_cli(["divide", "7.5", "2.5"])
    assert returncode == 0
    assert pytest.approx(float(stdout)) == 3.0
    assert stderr == ""

# --- Error Test Cases ---

def test_cli_invalid_operation() -> None:
    """Test CLI with an invalid operation name."""
    returncode, stdout, stderr = run_cli(["power", "2", "3"])
    assert returncode != 0
    assert stdout == ""
    assert "Invalid operation" in stderr

def test_cli_non_numeric_input() -> None:
    """Test CLI with non-numeric input for operands."""
    returncode, stdout, stderr = run_cli(["add", "abc", "10"])
    assert returncode != 0
    assert stdout == ""
    assert "invalid float value" in stderr

def test_cli_missing_arguments() -> None:
    """Test CLI with missing arguments."""
    returncode, stdout, stderr = run_cli(["add", "10"])
    assert returncode != 0
    assert stdout == ""
    assert "the following arguments are required" in stderr

def test_cli_division_by_zero() -> None:
    """Test CLI division by zero, expecting an error."""
    returncode, stdout, stderr = run_cli(["divide", "10", "0"])
    assert returncode != 0
    assert stdout == ""
    assert "Division by zero" in stderr
