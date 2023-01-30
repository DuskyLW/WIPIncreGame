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

from Buyable import Buyable
from Resource import Resource


class Producer(Buyable):

    def __init__(self, name, cost, production, amount=0, cap=-1,
                 ratio=1, flavText=None):
        Buyable.__init__(self, name,cost, amount=amount, cap=cap, ratio=ratio, flavText=flavText)
        self.production = production

    def produce(self, delta=1):
        linear = sum(self.getModifiers("linear_production"))
        multiplier = 1
        for i in self.getModifiers("multiplier_production"):
            multiplier*= i
        for resource in self.production:
            resource.add((self.production[resource] + linear)*self.amount*multiplier*delta)

    def update(self, delta=1):
        self.produce(delta)

    def getProduction(self):
        return self.production

    def setProduction(self, production):
        self.production = production


if __name__ == "__main__":
    wood = Resource("Wood", 20000, 20000)
    stone = Resource("Stone", 0, 20000)
    producer = Producer("Worker", {wood: 10}, {stone: 1}, ratio=2)
    print(producer, producer.getAmount())
    print(wood, wood.getAmount())
    print(stone, stone.getAmount())
    producer.buy()
    print(producer, producer.getAmount())
    print(wood, wood.getAmount())
    print(stone, stone.getAmount())
    producer.produce()
    print(producer, producer.getAmount())
    print(wood, wood.getAmount())
    print(stone, stone.getAmount())
    producer.buy()
    producer.multiply(2)
    producer.produce()
    print(producer, producer.getAmount())
    print(wood, wood.getAmount())
    print(stone, stone.getAmount())
