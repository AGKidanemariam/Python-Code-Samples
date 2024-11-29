# Ask the user for the current time (0-23) and the number of hours to wait
str_time = input("What time is it now (in hours 0-23)? ")
str_wait_time = input("What is the number of hours to wait? ")

# Convert the input strings to integers for calculation
time = int(str_time)
wait_time = int(str_wait_time)

# Calculate the time when the alarm will go off, wrapping around a 24-hour clock
time_when_alarm_go_off = (time + wait_time) % 24

# Output the result in a readable format
print(f"The alarm will go off at: {time_when_alarm_go_off}:00")
