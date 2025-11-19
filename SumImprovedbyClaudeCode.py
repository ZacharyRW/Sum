def get_number(prompt):
    """Get a valid number from user with error handling."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def demonstrate_sum_methods():
    """Demonstrate different approaches to summing two numbers."""
    
    print("=== Method 1: Convert input immediately ===")
    x = get_number('Enter first number: ')
    y = get_number('Enter second number: ')
    result1 = x + y
    print(f"Sum: {x} + {y} = {result1}\n")
    
    print("=== Method 2: Convert during calculation ===")
    w = input('Enter first number: ')
    z = input('Enter second number: ')
    try:
        result2 = int(w) + int(z)
        print(f"Sum: {w} + {z} = {result2}\n")
    except ValueError:
        print("Error: One or both inputs were not valid numbers.\n")
    
    print("=== Method 3: Using a dedicated function ===")
    a = get_number('Enter first number: ')
    b = get_number('Enter second number: ')
    result3 = sum([a, b])  # Using Python's built-in sum function
    print(f"Sum: {a} + {b} = {result3}\n")


if __name__ == "__main__":
    demonstrate_sum_methods()
