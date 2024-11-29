
# Abraham Kidanemariam
# 11/15/24
# Problem 3: Continuously ask the user for numbers until their sum exceeds 100.

numbers = []  # Initialize an empty list for user inputs
total = 0  # Initialize the sum

while total <= 100:
    number = int(input("Enter a number: "))  # Get a number from the user
    numbers.append(number)  # Append it to the list
    total += number  # Add it to the total sum

print("The numbers entered are:", numbers)
print("The total sum is:", total)
