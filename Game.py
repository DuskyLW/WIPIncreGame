import time
import os
import keyboard
from Resource import Resource


class Game:

    def __init__(self):
        self.resource = Resource("Stone", -1, 0)
        self.workers = 0
        self.workerability = 1
        self.workercost = 20
        self.displayworkerwarning = 0

    def keyboardlistners(self):
        keyboard.on_release_key("space", self.playerfarmresource)
        keyboard.on_release_key("w", self.buyworkers)

    def playerfarmresource(self, keyInfo):
        self.resource.add(1)

    def buyworkers(self, keyInfo):
        if self.resource.spend(self.workercost):
            self.workers += 1
        else:
            displayworkerwarning = 20

    def updateworkers(self):
        self.resource.add(self.workers * self.workerability)

    def display(self):
        os.system('cls')
        print("You currently have", self.workers, "workers.\n")
        self.resource.display()
        print("Press Spacebar to farm resource!\n")
        if self.resource.amount >= self.workercost or self.workers > 0:
            print("Press 'W' to buy a worker for",
                  self.workercost, "resource.")

    def update(self):
        self.updateworkers()

    def main(self):
        self.keyboardlistners()
        while True:
            self.update()
            self.display()
            time.sleep(.04)


if __name__ == "__main__":
    game = Game()
    game.main()
