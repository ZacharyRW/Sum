def get_number(prompt, allow_float=True):
    """Get a valid number from user with error handling (supports negative numbers)."""
    while True:
        try:
            user_input = input(prompt)
            if allow_float:
                return float(user_input)
            else:
                return int(user_input)
        except ValueError:
            number_type = "number" if allow_float else "whole number"
            print(f"Invalid input. Please enter a valid {number_type} (negative numbers allowed).")


def get_multiple_numbers(count, allow_float=True):
    """Get multiple numbers from the user."""
    numbers = []
    for i in range(count):
        num = get_number(f'Enter number {i + 1}: ', allow_float)
        numbers.append(num)
    return numbers


def method_two_integers():
    """Sum two integers."""
    print("\n=== Sum Two Integers ===")
    x = get_number('Enter first number: ', allow_float=False)
    y = get_number('Enter second number: ', allow_float=False)
    result = x + y
    print(f"Sum: {x} + {y} = {result}")


def method_two_floats():
    """Sum two floating-point numbers."""
    print("\n=== Sum Two Floats ===")
    a = get_number('Enter first number: ')
    b = get_number('Enter second number: ')
    result = a + b
    print(f"Sum: {a} + {b} = {result}")


def method_multiple_numbers():
    """Sum multiple numbers."""
    print("\n=== Sum Multiple Numbers ===")
    count = get_number('How many numbers do you want to sum? ', allow_float=False)
    if count < 1:
        print("Please enter at least 1 number.")
        return
    
    numbers = get_multiple_numbers(int(count))
    result = sum(numbers)
    
    numbers_str = ' + '.join(str(n) for n in numbers)
    print(f"Sum: {numbers_str} = {result}")


def method_custom_sum():
    """Custom summation implementation."""
    print("\n=== Custom Summation Function ===")
    count = get_number('How many numbers? ', allow_float=False)
    if count < 1:
        print("Please enter at least 1 number.")
        return
    
    numbers = get_multiple_numbers(int(count))
    
    def custom_sum(nums):
        """Custom implementation of sum without using built-in."""
        total = 0
        for num in nums:
            total += num
        return total
    
    result = custom_sum(numbers)
    numbers_str = ' + '.join(str(n) for n in numbers)
    print(f"Sum: {numbers_str} = {result}")


def method_positive_negative_demo():
    """Demonstrate summing positive and negative numbers."""
    print("\n=== Positive and Negative Numbers Demo ===")
    print("Enter a mix of positive and negative numbers")
    count = get_number('How many numbers? ', allow_float=False)
    if count < 1:
        print("Please enter at least 1 number.")
        return
    
    numbers = get_multiple_numbers(int(count))
    result = sum(numbers)
    
    positive_nums = [n for n in numbers if n > 0]
    negative_nums = [n for n in numbers if n < 0]
    zero_nums = [n for n in numbers if n == 0]
    
    numbers_str = ' + '.join(str(n) for n in numbers)
    print(f"\nSum: {numbers_str} = {result}")
    print(f"\nBreakdown:")
    print(f"  Positive numbers: {positive_nums} (sum: {sum(positive_nums) if positive_nums else 0})")
    print(f"  Negative numbers: {negative_nums} (sum: {sum(negative_nums) if negative_nums else 0})")
    if zero_nums:
        print(f"  Zeros: {len(zero_nums)}")


def display_menu():
    """Display the main menu."""
    print("\n" + "="*50)
    print("Python Number Summation Examples")
    print("="*50)
    print("1. Sum two integers")
    print("2. Sum two floats")
    print("3. Sum multiple numbers")
    print("4. Custom summation function")
    print("5. Positive/Negative numbers demo")
    print("6. Run all examples")
    print("0. Exit")
    print("="*50)


def run_all_examples():
    """Run all example methods."""
    method_two_integers()
    input("\nPress Enter to continue...")
    method_two_floats()
    input("\nPress Enter to continue...")
    method_multiple_numbers()
    input("\nPress Enter to continue...")
    method_custom_sum()
    input("\nPress Enter to continue...")
    method_positive_negative_demo()


def main():
    """Main program loop with menu system."""
    while True:
        display_menu()
        choice = input("\nEnter your choice (0-6): ")
        
        if choice == '1':
            method_two_integers()
        elif choice == '2':
            method_two_floats()
        elif choice == '3':
            method_multiple_numbers()
        elif choice == '4':
            method_custom_sum()
        elif choice == '5':
            method_positive_negative_demo()
        elif choice == '6':
            run_all_examples()
        elif choice == '0':
            print("\nThank you for using the summation examples!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 0 and 6.")
        
        if choice in ['1', '2', '3', '4', '5']:
            input("\nPress Enter to return to menu...")


if __name__ == "__main__":
    main()
