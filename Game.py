import time
import os
import keyboard

class Game:

    def __init__(self):
        self.resource = 0
        self.workers = 0
        self.workerability = 1
        self.workercost = 20
        self.displayworkerwarning = 0

    def keyboardlistners(self):
        keyboard.on_release_key("space", self.playerfarmresource)
        keyboard.on_release_key("w", self.buyworkers)


    def playerfarmresource(self, keyInfo):
        self.resource += 1

    def buyworkers(self, keyInfo):
        if self.resource >= self.workercost:
            self.resource -= self.workercost
            self.workers += 1
            self.workercost = int(self.workercost * 1.5)
        else:
            self.displayworkerwarning = 20

    def updateworkers(self):
        self.resource += (self.workers * self.workerability)

    def display(self):
        os.system('cls')
        print("You currently have", self.workers, "workers.\n")
        print("You currently have", self.resource, "resource.")
        print("Press Spacebar to farm resource!\n")
        if self.resource >= self.workercost or self.workers > 0:
            print("Press 'W' to buy a worker for", self.workercost, "resource.")
        if self.displayworkerwarning > 0:
            if self.resource < self.workercost:
                print("Not enough resource!")
                self.displayworkerwarning -= 1
            else:
                self.displayworkerwarning = 0

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
