import time
import os
import keyboard
from Resource import Resource
from Producer import Producer
from Converter import Converter
from Upgrade import Upgrade


class Game:

    def __init__(self):
        self.resources = {"stone": Resource("Stone", 0, -1, True),
                          "wood": Resource("Wood", 10, -1),
                          "tool": Resource("Tool", 0, -1, True)}
        self.producers = {"worker":
                          Producer("Worker",
                                   {self.resources["wood"]: 10},
                                   {self.resources["wood"]: 1})
                          }
        self.converters = {"builder":
                           Converter("Builder",
                                     {self.resources["wood"]: 10},
                                     {self.resources["tool"]: 1},
                                     {self.resources["wood"]: 1})
                           }
        self.upgrades = {"better pay":
                         Upgrade("better pay",
                                 {self.resources["wood"]: 10},
                                 self.converters["builder"],
                                 lambda converter: converter.multiply(10))
                         }

    def keyboardlistners(self):
        keyboard.on_release_key("space", self.playerfarmresource)
        keyboard.on_release_key("w", self.buyworkers)
        keyboard.on_release_key("b", self.buybuilder)
        keyboard.on_release_key("c", self.convertertoggle)
        keyboard.on_release_key("x", self.buyUpgrade)

    def playerfarmresource(self, keyInfo):
        self.resources["wood"].add(1)

    def buyworkers(self, keyInfo):
        self.producers["worker"].buy()

    def buybuilder(self, keyInfo):
        self.converters["builder"].buy()

    def buyUpgrade(self, keyInfo):
        self.upgrades["better pay"].buy()

    def convertertoggle(self, keyInfo):
        self.converters["builder"].toggle()

    def display(self):
        os.system('cls')
        for resource in self.resources.values():
            resource.display()
        for producer in self.producers.values():
            producer.display()
        for converter in self.converters.values():
            converter.display()
        print("Press Spacebar to farm resource!\n")
        print(self.upgrades["better pay"])

    def update(self):
        for producer in self.producers.values():
            producer.update()
        for converter in self.converters.values():
            converter.update()

    def main(self):
        self.keyboardlistners()
        while True:
            self.update()
            self.display()
            time.sleep(.04)


if __name__ == "__main__":
    game = Game()
    game.main()
