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

from Resource import Resource


class Buyable:

    def __init__(self, name, cost, amount=0, ratio=1, flavText=None):
        self.cost = cost
        self.amount = amount
        self.name = name
        self.ratio = ratio
        self.flavText = flavText

    def canbuy(self):
        currentCost = self.getCurrentCost()
        for resource in currentCost:
            if not resource.canAfford(currentCost[resource]):
                return False
        return True

    def buy(self):
        currentCost = self.getCurrentCost()
        if self.canbuy():
            for resource in self.cost:
                resource.spend(currentCost[resource])
            self.amount += 1
            return True
        return False

    def buyX(self, buytimes):
        for singlebuy in range(buytimes):
            self.buy()

    def display(self):
        if (self.amount >= 1):
            print("You have {amount} {name}s".format(
                amount=self.amount, name=self.name))
        else:
            print("You have {amount} {name}".format(
                amount=self.amount, name=self.name))

    def getCost(self):
        return self.cost

    def setCost(self, cost):
        self.cost = cost

    def getAmount(self):
        return self.amount

    def setAmount(self, amount):
        self.amount = amount

    def getCurrentCost(self):
        currentCost = {}
        for resource in self.cost:
            currentCost[resource] = self.cost[resource]*self.ratio**self.amount
        return currentCost

    def getRatio(self):
        return self.ratio

    def setRatio(self, ratio):
        self.ratio = ratio

    def getFlavText(self):
        return self.flavText

    def setFlavText(self, flavText):
        self.flavText = flavText

    def __repr__(self):
        return self.name + " Buyable"


if __name__ == "__main__":
    wood = Resource("Wood", 20000, 20000)
    buyable = Buyable("buyable", {wood: 10})
    buyable.setRatio(2)
    print(buyable.getCurrentCost())
    buyable.buy()
    print(buyable.getCurrentCost())
    buyable.buy()
    print(buyable.getCurrentCost())
