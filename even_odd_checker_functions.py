# Function to handle user input and return an integer
def get_integer_input():
    # Prompt user to enter an integer
    user_input = input("Please enter an integer: ")
    
    # Convert the input to an integer and return it
    try:
        return int(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return get_integer_input()  # Recursively ask again if the input is not valid

# Function to determine if the given number is even or odd
def check_even_odd(number):
    # Check if the number is even or odd using modulo operator
    if number % 2 == 0:
        return f"{number} is an Even number."
    else:
        return f"{number} is an Odd number."

# Main program flow
def main():
    # Get integer input from the user
    number = get_integer_input()
    
    # Determine if the number is even or odd and display the result
    result = check_even_odd(number)
    print(result)

# Run the main program
if __name__ == "__main__":
    main()
