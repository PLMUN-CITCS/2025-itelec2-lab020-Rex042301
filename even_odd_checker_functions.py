# even_odd_checker_functions.py

def get_integer_input() -> int:
    """
    This function prompts the user to enter an integer. It ensures that the input is a valid integer.
    
    Returns:
        int: The integer entered by the user.
    """
    while True:
        try:
            number = int(input("Enter an integer: "))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def check_even_odd(number: int) -> str:
    """
    This function checks if a given number is even or odd.
    
    Args:
        number (int): The number to be checked.
        
    Returns:
        str: A formatted string message indicating whether the number is even or odd.
    """
    if number % 2 == 0:
        return f"{number} is an Even number."
    else:
        return f"{number} is an Odd number."

def main():
    """
    Main program flow.
    Calls the get_integer_input function to get the integer and then check_even_odd to determine if it's even or odd.
    Displays the result to the user.
    """
    number = get_integer_input()  # Get the integer from the user
    result = check_even_odd(number)  # Check if the number is even or odd
    print(result)  # Output the result to the user

if __name__ == "__main__":
    main()
