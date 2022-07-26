import time
import os
import keyboard
from Resource import Resource
from Producer import Producer


class Game:

    def __init__(self):
        self.resources = [Resource("Stone", -1, 0, True), Resource("Wood", -1, 10)]
        self.producers = [Producer([self.resources[0]], [20], 0, [
                                   self.resources[0]], [1], "Worker")]

    def keyboardlistners(self):
        keyboard.on_release_key("space", self.playerfarmresource)
        keyboard.on_release_key("w", self.buyworkers)

    def playerfarmresource(self, keyInfo):
        self.resources[0].add(1)

    def buyworkers(self, keyInfo):
        self.producers[0].buy()

    def display(self):
        os.system('cls')
        for resource in self.resources:
            resource.display()
        for producer in self.producers:
            producer.display()
        print("Press Spacebar to farm resource!\n")

    def update(self):
        for producer in self.producers:
            producer.produce()

    def main(self):
        self.keyboardlistners()
        while True:
            self.update()
            self.display()
            time.sleep(.04)


if __name__ == "__main__":
    game = Game()
    game.main()
