import time
import os
resource = 0
workers = 1
workerability = 1


def buyworkers():
    global workers
    global resource
    if resource > 20:
        resource -= 20
        workers += 1


def updateworkers():
    global resource
    resource += (workers * workerability)


def update():
    updateworkers()
    buyworkers()
    os.system('cls')
    print("You currently have", workers, "workers.\n")
    print("You currently have", resource, "resource.")
    pass


def main():
    while True:
        update()
        time.sleep(.1)


if __name__ == "__main__":
    main()
