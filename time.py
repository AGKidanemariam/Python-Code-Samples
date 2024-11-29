# Ask the user for the current time (in 24-hour format) and the wait time (in hours)
current_time_str = input("What is the current time (in hours 0-23)? ")
wait_time_str = input("How many hours do you want to wait? ")

# Convert the input strings to integers
current_time_int = int(current_time_str)
wait_time_int = int(wait_time_str)

# Calculate the final time after the wait, accounting for the 24-hour clock
final_time_int = (current_time_int + wait_time_int) % 24

# Output the final time
print(f"The time after {wait_time_int} hours will be: {final_time_int}:00")

