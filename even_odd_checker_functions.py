# Function to handle user input and return an integer
def get_integer_input():
    user_input = input("Please enter an integer: ")
    
    try:
        return int(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return get_integer_input()

def check_even_odd(number: float) -> str:
    if number % 2 == 0:
        return(f"the {number} is an Even number.")
    if number % 2 == 1:
        return(f" the {number} is an Odd number.") 
    # Main program flow
def main():
    number = get_integer_input()
    result = check_even_odd(number)
    print(result)

# Run the main program
if __name__ == "__main__":
    main()
