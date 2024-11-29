# This program checks if the user is a pirate by comparing their password.

greeting = input("Hello, possible pirate! What's the password? ").strip().lower()  
# strip() removes leading/trailing spaces, lower() makes it case-insensitive

if greeting == "arrr!":
    print("Go away, pirate.")
else:
    print("Greetings, hater of pirates!")
