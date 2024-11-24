#writing a program to check if number is even or odd.
def check_even_or_odd(number):
    """Function to determine if the number is even or odd."""
    if number % 2 == 0:
        return f"The number {number} is even."
    else:
        return f"The number {number} is odd."

def main():
    """Main function to execute the program."""
# Asking user for a number.
    user_input = int(input("Please enter a number: "))
# Calling the function with the user's input.
    result = check_even_or_odd(user_input)
# Printing the result.
    print(result)

if __name__ == "__main__":
    main()