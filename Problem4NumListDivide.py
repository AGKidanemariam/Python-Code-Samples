
# Abraham Kidanemariam
# 11/15/24
# Problem 4: Collect numbers divisible by 10 up to 50 in a list.

tens = []  # Initialize an empty list for multiples of 10
counter = 0  # Initialize the counter

while counter <= 50:
    if counter % 10 == 0:  # Check if the counter is divisible by 10
        tens.append(counter)  # Append the value to the list
    counter += 1  # Increment the counter

print("Numbers divisible by 10:", tens)
