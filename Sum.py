def main():
    """Demonstrate two methods of summing numbers from user input."""
    # Method 1: Convert immediately
    x = int(input('Enter first number: '))
    y = int(input('Enter second number: '))
    result1 = x + y
    print(f"Method 1 result: {result1}")

    # Method 2: Convert during operation
    w = input('Enter first number: ')
    z = input('Enter second number: ')
    result2 = int(w) + int(z)
    print(f"Method 2 result: {result2}")


if __name__ == "__main__":
    main()
