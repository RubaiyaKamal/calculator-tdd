import argparse
import sys
from calculator import add, subtract, multiply, divide

def main() -> None:
    parser = argparse.ArgumentParser(description="Perform basic arithmetic operations.")
    parser.add_argument("operation", type=str, help="Operation to perform (add, subtract, multiply, divide)")
    parser.add_argument("num1", type=float, help="First number")
    parser.add_argument("num2", type=float, help="Second number")

    args = parser.parse_args()

    try:
        result: float | int
        if args.operation == "add":
            result = add(args.num1, args.num2)
        elif args.operation == "subtract":
            result = subtract(args.num1, args.num2)
        elif args.operation == "multiply":
            result = multiply(args.num1, args.num2)
        elif args.operation == "divide":
            if args.num2 == 0:
                raise ValueError("Division by zero is not allowed.")
            result = divide(args.num1, args.num2)
        else:
            raise ValueError(f"Invalid operation: {args.operation}")
        
        print(result)
    except TypeError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()