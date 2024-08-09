#Abraham Kidanemariam
#7/19/2024
# Problem 1 - prints “Hello World” to the screen
print ("Hello World")

# Problem 2 - asks the user for their name and greets them with their name
x = input ("Please enter your name: ")
print ("Good morning " + x)

# Problem 3 - only the users you and your instructor are greeted with their names
# Program to compute the sum or product of two numbers based on user choice
def compute_sum_or_product():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    choice = input("Enter 1 to compute the sum, 2 to compute the product: ")

    if choice == '1':
        result = num1 + num2
        print(f"The sum is: {result}")
    elif choice == '2':
        result = num1 * num2
        print(f"The product is: {result}")
    else:
        print("Invalid choice")

# Call the function
compute_sum_or_product()

#computes the sum or product of two numbers based on the user's choice:
# Program to compute the sum or product of two numbers based on user choice
def compute_sum_or_product():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    choice = input("Enter 1 to compute the sum, 2 to compute the product: ")

    if choice == '1':
        result = num1 + num2
        print(f"The sum is: {result}")
    elif choice == '2':
        result = num1 * num2
        print(f"The product is: {result}")
    else:
        print("Invalid choice")

# Call the function
compute_sum_or_product()

