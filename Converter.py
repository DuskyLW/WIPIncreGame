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

from Producer import Producer
from Consumer import Consumer
from Resource import Resource


class Converter(Producer, Consumer):
    def __init__(self, name, cost, production, consumption, enabled=False,
                 amount=0, cap=-1, ratio=1, flavText=None):
        Producer.__init__(self, name, cost, production, amount=amount, cap=cap,
                         ratio=ratio, flavText=flavText)
        self.amount = amount
        self.consumption = consumption
        self.enabled = enabled
        self.consumeAll = False

    def convert(self, delta):
            consumptionFactor = self.consume(delta)
            self.produce(delta * consumptionFactor)

    def update(self, delta):
        if self.enabled:
            self.convert(delta)

    def toggle(self):
        if self.enabled:
            self.enabled = False
        else:
            self.enabled = True


if __name__ == "__main__":
    wood = Resource("Wood", 20000, 20000)
    stone = Resource("Stone", 0, 20000)
    converter = Converter("Converter", {wood: 1}, {
                          stone: 10}, {wood: 1}, enabled=True, amount=0)
    print(converter, converter.getAmount())
    print(wood, wood.getAmount())
    print(stone, stone.getAmount())
    converter.update(1)
    print(converter, converter.getAmount())
    print(wood, wood.getAmount())
    print(stone, stone.getAmount())
    converter.setAmount(10)
    converter.update(1)
    print(converter, converter.getAmount())
    print(wood, wood.getAmount())
    print(stone, stone.getAmount())