# Function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

# Taking input from the user
number = int(input("Enter a number: "))
check_even_odd(number)
