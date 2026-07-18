def get_number(prompt):
    """Get a valid whole number, or return ``None`` when input is closed."""
    while True:
        try:
            return int(input(prompt))
        except EOFError:
            print("Input closed. Exiting this demo.")
            return None
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def demonstrate_sum_methods():
    """Demonstrate different approaches to summing two numbers."""
    
    print("=== Method 1: Convert input immediately ===")
    x = get_number('Enter first number: ')
    y = get_number('Enter second number: ')
    if x is None or y is None:
        return
    result1 = x + y
    print(f"Sum: {x} + {y} = {result1}\n")
    
    print("=== Method 2: Convert during calculation ===")
    try:
        w = input('Enter first number: ')
        z = input('Enter second number: ')
        result2 = int(w) + int(z)
        print(f"Sum: {w} + {z} = {result2}\n")
    except ValueError:
        print("Error: One or both inputs were not valid numbers.\n")
    except EOFError:
        print("Input closed. Exiting this demo.")
        return
    
    print("=== Method 3: Using a dedicated function ===")
    a = get_number('Enter first number: ')
    b = get_number('Enter second number: ')
    if a is None or b is None:
        return
    result3 = sum([a, b])  # Using Python's built-in sum function
    print(f"Sum: {a} + {b} = {result3}\n")


if __name__ == "__main__":
    demonstrate_sum_methods()
