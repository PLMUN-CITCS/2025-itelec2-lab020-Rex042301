def get_integer_input() -> int:
    """
    Prompt the user to enter an integer. 
    This function will repeatedly ask for input until a valid integer is provided.

    Returns:
        int: The valid integer input from the user.
    """
    while True:
        try:
            # Attempt to convert the input to an integer
            user_input = int(input("Enter an integer: "))
            return user_input
        except ValueError:
            # If input is not a valid integer, print an error message and prompt again
            print("Invalid input. Please enter a valid integer.")

def check_even_odd(number: int) -> str:
    """
    Determines whether a given integer is even or odd.
    
    Args:
        number (int): The number to check.
    
    Returns:
        str: A formatted string indicating whether the number is even or odd.
    """
    if number % 2 == 0:
        return f"{number} is an Even number."
    else:
        return f"{number} is an Odd number."

# Main program flow
def main():
    # Get the integer input from the user
    number = get_integer_input()
    
    # Check if the number is even or odd
    result = check_even_odd(number)
    
    # Display the result to the user
    print(result)

if __name__ == "__main__":
    main()
