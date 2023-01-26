#   Written by Dallin Dmytryk, Charlie Yeudall 2022
#
#    Copyright 2022 Dallin Dmytryk, Charlie Yeudall
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import time
import os
import keyboard
from Resource import Resource
from Producer import Producer
from Converter import Converter
from Upgrade import Upgrade
from Modifier import Modifier


class Game:

    def __init__(self):
        self.tickspeed = 1
        self.resources = {"stone": Resource("Stone", 0, -1, True),
                          "wood": Resource("Wood", 10, -1),
                          "tool": Resource("Tool", 0, -1, True)}
        self.producers = {"worker":
                          Producer("Worker",
                                   {self.resources["wood"]: 1},
                                   {self.resources["wood"]: 1})
                          }
        self.converters = {"builder":
                            Converter("builders", 
                                    {self.resources["wood"]: 10},
                                    {self.resources["stone"]: 1},
                                    {self.resources["wood"]:2},
                                    enabled=True)
                            }
        self.upgrades = {"better pay": 
                            Upgrade("Better Pay", 
                                    {self.resources["stone"]: 1},
                                    self.producers["worker"],
                                    lambda target: target.addModifier(Modifier(lambda items: 100), "multiplier_production")),
                        "replication":
                            Upgrade("Replication",
                                    {self.resources["wood"]: 200},
                                    self.producers["worker"],
                                    lambda target: target.addModifier(Modifier(lambda items: items.getAmount(), self.producers["worker"]), "linear_production")) 
                            
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
        self.upgrades["replication"].buy()    

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
            print(converter.enabled)
        print("Press Spacebar to farm resource!\n")
        print(self.upgrades["better pay"])

    def update(self, delta):
        for producer in self.producers.values():
            producer.update(delta)
        for converter in self.converters.values():
            converter.update(delta)

    def main(self):
        self.keyboardlistners()
        lastTime = time.time()
        while True:
            currentTime = time.time()
            delta = (currentTime-lastTime)/self.tickspeed
            lastTime=currentTime
            self.update(delta)
            self.display()


if __name__ == "__main__":
    game = Game()
    game.main()
