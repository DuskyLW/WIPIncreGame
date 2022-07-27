import time
import os
import keyboard
from Resource import Resource
from Producer import Producer
from Converter import Converter
from Upgrade import Upgrade


class Game:

    def __init__(self):
        self.resources = [Resource("Stone", -1, 0, True),
                          Resource("Wood", -1, 10), Resource("Tool", -1, 0, True)]
        self.producers = [Producer([self.resources[0]], [20], 0, [
                                   self.resources[0]], [1], "Worker")]
        self.converters = [Converter([self.resources[0]], [20], 0, [
            self.resources[0]], [1], "Builder", [self.resources[2]], [1])]
        self.upgrades = [Upgrade([self.resources[1]], [1], 0,
                                 self.producers[0], lambda producer: producer.setMult(100), "Better Pay")]

    def keyboardlistners(self):
        keyboard.on_release_key("space", self.playerfarmresource)
        keyboard.on_release_key("w", self.buyworkers)
        keyboard.on_release_key("b", self.buybuilder)
        keyboard.on_release_key("c", self.convertertoggle)
        keyboard.on_release_key("x", self.buyUpgrade)

    def playerfarmresource(self, keyInfo):
        self.resources[0].add(1)

    def buyworkers(self, keyInfo):
        self.producers[0].buy()

    def buybuilder(self, keyInfo):
        self.converters[0].buy()

    def buyUpgrade(self, keyInfo):
        self.upgrades[0].buy()

    def convertertoggle(self, keyInfo):
        self.converters[0].toggle()

    def display(self):
        os.system('cls')
        for resource in self.resources:
            resource.display()
        for producer in self.producers:
            producer.display()
        for converter in self.converters:
            converter.display()
        print("Press Spacebar to farm resource!\n")

    def update(self):
        for producer in self.producers:
            producer.produce()
        for converter in self.converters:
            converter.convert()

    def main(self):
        self.keyboardlistners()
        while True:
            self.update()
            self.display()
            time.sleep(.04)


if __name__ == "__main__":
    game = Game()
    game.main()
