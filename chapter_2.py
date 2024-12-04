
def arrive_at_engineering_bay():
    print("You arrive at the engineering bay, but it's under attack!")

def fight_invaders():
    print("You fight off the invaders bravely.")
    return True  # Assume victory for simplicity

def secure_bay():
    print("You secure the engineering bay and gather provisions.")

def chapter_2():
    print("=== Chapter 2: Engineering Bay Under Siege ===")
    arrive_at_engineering_bay()
    if fight_invaders():
        secure_bay()
    print("Proceeding to Chapter 3...")
