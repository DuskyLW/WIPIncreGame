import time
import os
import keyboard
resource = 0
workers = 0
workerability = 1
workercost = 20
displayworkerwarning = 0


def keyboardlistners():
    keyboard.on_release_key("space", playerfarmresource)
    keyboard.on_release_key("w", buyworkers)


def playerfarmresource(self):
    global resource
    resource += 1


def buyworkers(self):
    global workers
    global resource
    global workercost
    global displayworkerwarning
    if resource >= workercost:
        resource -= workercost
        workers += 1
        workercost *= 2
    else:
        displayworkerwarning = 20


def updateworkers():
    global resource
    resource += (workers * workerability)


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


def update():
    updateworkers()


def main():
    keyboardlistners()
    while True:
        update()
        display()
        time.sleep(.04)


if __name__ == "__main__":
    main()

# testing
