# Function to handle user input and return an integer
def get_integer_input():
    user_input = input("Please enter an integer: ")
    
    try:
        return int(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return get_integer_input()

def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is an Even number."
    if number % 2 == 1:
        return f"{number} is an Odd number."
    else: 
        return f"{user_input} is invalid."
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
