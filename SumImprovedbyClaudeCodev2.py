def get_number(prompt, allow_float=True):
    """Get a valid number from user with error handling."""
    while True:
        try:
            user_input = input(prompt)
            if allow_float:
                return float(user_input)
            else:
                return int(user_input)
        except ValueError:
            number_type = "number" if allow_float else "whole number"
            print(f"Invalid input. Please enter a valid {number_type}.")


def get_multiple_numbers(count, allow_float=True):
    """Get multiple numbers from the user."""
    numbers = []
    for i in range(count):
        num = get_number(f'Enter number {i + 1}: ', allow_float)
        numbers.append(num)
    return numbers


def demonstrate_sum_methods():
    """Demonstrate different approaches to summing numbers."""
    
    print("=== Method 1: Sum two integers ===")
    x = get_number('Enter first number: ', allow_float=False)
    y = get_number('Enter second number: ', allow_float=False)
    result1 = x + y
    print(f"Sum: {x} + {y} = {result1}\n")
    
    print("=== Method 2: Sum two floats ===")
    a = get_number('Enter first number: ')
    b = get_number('Enter second number: ')
    result2 = a + b
    print(f"Sum: {a} + {b} = {result2}\n")
    
    print("=== Method 3: Sum multiple numbers ===")
    count = get_number('How many numbers do you want to sum? ', allow_float=False)
    if count < 1:
        print("Please enter at least 1 number.\n")
        return
    
    numbers = get_multiple_numbers(int(count))
    result3 = sum(numbers)
    
    # Format output nicely
    numbers_str = ' + '.join(str(n) for n in numbers)
    print(f"Sum: {numbers_str} = {result3}\n")
    
    print("=== Method 4: Custom summation function ===")
    more_numbers = get_multiple_numbers(3)
    
    def custom_sum(nums):
        """Custom implementation of sum without using built-in."""
        total = 0
        for num in nums:
            total += num
        return total
    
    result4 = custom_sum(more_numbers)
    numbers_str = ' + '.join(str(n) for n in more_numbers)
    print(f"Sum: {numbers_str} = {result4}\n")


if __name__ == "__main__":
    print("Python Number Summation Examples\n")
    demonstrate_sum_methods()
