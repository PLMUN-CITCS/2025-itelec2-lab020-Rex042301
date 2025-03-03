# even_odd_checker_functions.py

def get_integer_input():
    """Prompts the user to enter an integer and returns it."""
    while True:
        try:
            user_input = input("Enter an integer: ")
            # Convert the input to an integer
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def check_even_odd(number):
    """Determines if a number is even or odd."""
    if number % 2 == 0:
        return f"{number} is an Even number."
    else:
        return f"{number} is an Odd number."

# Main Program Flow
if __name__ == "__main__":
    number = get_integer_input()  # Get the user's input
    result = check_even_odd(number)  # Check if the number is even or odd
    print(result)  # Output the result
