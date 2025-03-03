# even_odd_checker.py

def get_integer_input():
    # Get integer input from the user
    user_input = input("Enter an integer: ")
    return int(user_input)

def check_even_odd(number):
    # Check if the number is even or odd
    if number % 2 == 0:
        return f"{number} is an Even number."
    else:
        return f"{number} is an Odd number."

# Main Program Flow
number = get_integer_input()
result = check_even_odd(number)
print(result)
