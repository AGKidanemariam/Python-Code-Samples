
def enter_control_room():
    print("You enter the control room. It's bustling with activity.")

def interact_with_crew():
    print("You gather information from the crew about potential attacks.")

def check_surveillance():
    print("The surveillance system reveals enemy positions.")

def prepare_defenses():
    print("Defenses are prepared. Setting traps...")
    traps_set = True
    return traps_set

def chapter_1():
    print("=== Chapter 1: Control Room and Initial Defense ===")
    enter_control_room()
    interact_with_crew()
    check_surveillance()
    traps_set = prepare_defenses()
    if traps_set:
        print("Traps successfully set. You'll gain an advantage in Chapter 2.")
    print("Proceeding to Chapter 2...")
