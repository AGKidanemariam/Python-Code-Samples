# Abraham Kidanemariam
# 11/10/24
# Problem 3: Write a Python function to multiply all the numbers in a list. Use list [5, 2, 7, -1].

def multiply_list(lst):
    """Multiplies all numbers in a list."""
    result = 1
    for number in lst:
        result *= number
    return result

# Testing the function
test_list = [5, 2, 7, -1]
print(f"The product of {test_list} is {multiply_list(test_list)}")
