import time
import os
resource = 0


def update():
    global resource
    os.system('cls')
    resource += 1
    print("You currently have", resource, "resource.")
    pass


def main():
    while True:
        update()
        time.sleep(.1)


if __name__ == "__main__":
    main()
