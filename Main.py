# Base imports
import time
import os
import keyboard
# Base variables
resource = 0
workers = 0
workerability = 1
workercost = 20
displayworkerwarning = 0

# Checks for player inputs


def keyboardlistners():
    keyboard.on_release_key("space", playerfarmresource)
    keyboard.on_release_key("w", buyworkers)

# Lets player farm resource themselves


def playerfarmresource(self):
    global resource
    resource += 1

# Lets player buy workers to farm resource for them


def buyworkers(self):
    global workers
    global resource
    global workercost
    global displayworkerwarning
    if resource >= workercost:
        resource -= workercost
        workers += 1
        workercost = int(workercost * 1.5)
    else:
        displayworkerwarning = 20

# Applies worker's labor into resource count


def updateworkers():
    global resource
    resource += (workers * workerability)

# Handles text output to screen


def display():
    global resource
    global displayworkerwarning
    os.system('cls')
    print("You currently have", workers, "workers.\n")
    print("You currently have", resource, "resource.")
    print("Press Spacebar to farm resource!\n")
    if resource >= workercost or workers > 0:
        print("Press 'W' to buy a worker for", workercost, "resource.")
    if displayworkerwarning > 0:
        if resource < workercost:
            print("Not enough resource!")
            displayworkerwarning -= 1
        else:
            displayworkerwarning = 0

# Function for handling program updates per loop


def update():
    updateworkers()

# Main loop where everything is executed


def main():
    keyboardlistners()
    while True:
        update()
        display()
        time.sleep(.04)


if __name__ == "__main__":
    main()
