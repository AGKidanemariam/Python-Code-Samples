# Abraham Kidanemariam
# 11/10/24
# Problem 4: Write a Python function that takes a list and returns a list of unique elements.

def unique_elements(lst):
    """Returns a list of unique elements from the given list."""
    unique_list = []
    for number in lst:
        if number not in unique_list:
            unique_list.append(number)
    return unique_list

# Testing the function
test_list = [1, 3, 3, 3, 6, 2, 3, 5]
print(f"The unique elements in {test_list} are {unique_elements(test_list)}")

