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


class Consumer(Buyable):

    def __init__(self, name, cost, consumption, amount=0, cap=-1,
                 ratio=1, flavText=None, consumeAll=False):
        super().__init__(name, cost, amount=amount, cap=cap, ratio=ratio, flavText=flavText)
        self.consumption = consumption
        self.consumeAll = consumeAll

    def consume(self, delta=1):
        linear = sum(self.getModifiers("linear_consumption"))
        multiplier = 1
        for i in self.getModifiers("multiplier_consumption"):
            multiplier*= i
        consumptionFactor = 1
        if not self.consumeAll:
            for resource in self.consumption:
                consumptionFactor = min(resource.getSpendPercent((self.consumption[resource] + linear)*self.amount*multiplier*delta), consumptionFactor)
        for resource in self.consumption:
            spendAmount = (self.consumption[resource] + linear)*self.amount*multiplier*delta*consumptionFactor
            resource.spend((self.consumption[resource] + linear)*self.amount*multiplier*delta*consumptionFactor)
        return consumptionFactor

    def update(self, delta=1):
        self.consume(delta)

    def getConsumption(self):
        return self.consumption

    def setConsumption(self, consumption):
        self.consumption = consumption


if __name__ == "__main__":
    consumer = Consumer("consumer", {},{},0)
    print(consumer.amount)
