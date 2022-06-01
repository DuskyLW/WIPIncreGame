import os
import time
import keyboard
apples = 0


def updatething():
    global apples


def addapple(self):
    global apples
    apples += 1


def update():
    updatething()
    os.system('cls')
    if apples == 0:
        print("You currently have", apples, "apples.")
    elif apples == 1:
        print("You currently have", apples, "apple.")
    else:
        print("You currently have", apples, "apples.")


def main():
    keyboard.on_release_key("space", addapple)
    while True:
        update()
        time.sleep(0.04)


if __name__ == "__main__":
    main()
