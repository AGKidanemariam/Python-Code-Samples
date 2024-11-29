# Abraham Kidanemariam
# 11/10/24
# Problem 2: Write a Python function to check whether a number is in a given range (1 to 10).

def check_range(num):
    """Checks if a number is in the range 1 to 10."""
    if num in range(1, 10):
        print(f"{num} is in the range.")
    else:
        print(f"{num} is not in the range.")

# Testing the function
check_range(5)
check_range(12)
