# Corrected FizzBuzz implementation
def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 15 == 0:  # First, check for divisibility by both 3 and 5
            print("FizzBuzz", end=' ')
        elif i % 3 == 0:  # Next, check for divisibility by 3
            print("Fizz", end=' ')
        elif i % 5 == 0:  # Then, check for divisibility by 5
            print("Buzz", end=' ')
        else:  # If none of the conditions are met, print the number itself
            print(i, end=' ')
    print()  # Add a newline for readability


# Entry point of the script
if __name__ == "__main__":
    import sys

    # Check if a command-line argument is provided for the range limit
    if len(sys.argv) == 2:
        try:
            n = int(sys.argv[1])
            fizzbuzz(n)  # Call the fizzbuzz function with the provided limit
        except ValueError:
            print("Usage: python 0-fizzbuzz.py <number>")
            print("<number> should be an integer.")
    else:
        print("Usage: python 0-fizzbuzz.py <number>")
        print("Please provide a single integer argument for the range limit.")
