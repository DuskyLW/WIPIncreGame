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

    # Takes a name for the buyable object, cost to buy, the amount that has
    # already been bought/ current iteration of amount of times bought, a ratio
    # that describes how much extra each new upgrade will cost, and a flavor
    # text for the object.
    def __init__(self, name, cost, amount=0, ratio=1, flavText=None):
        self.name = name
        self.cost = cost
        self.amount = amount
        self.ratio = ratio
        self.flavText = flavText

# Using an empty dictionary, we iterate through the resources that are buyable
# and return the current cost of each buyable thing using the formula of taking
# the current cost, mulitplying that by the ratio or amount extra to cost each
# new buy and do exponent based on the amount of times object has been bought.
    def getCurrentCost(self):
        currentCost = {}
        for resource in self.cost:
            currentCost[resource] = self.cost[resource]*self.ratio**self.amount
        return currentCost

# Assigns currentCost a value based on result from getCurrentCost method. Based
# on the result of the canAfford method from resource, if we can't afford then
# return false, otherwise return True.
    def canbuy(self):
        currentCost = self.getCurrentCost()
        for resource in currentCost:
            if not resource.canAfford(currentCost[resource]):
                return False
        return True

# Assigns currentCost a value based on result from getCurrentCost method. If
# we can afford buying, perform the spend method from resource to perform the
# buy, then increment the amount of times bought by 1 and return True.
# Otherwise return False.
    def buy(self):
        currentCost = self.getCurrentCost()
        if self.canbuy():
            for resource in self.cost:
                resource.spend(currentCost[resource])
            self.amount += 1
            return True
        return False

# Function that performs the buy method as many times as specficied by the
# argument. Using a for loop to iterate through a range of numbers as long
# as the argument inputted as a means of repeating the method.
    def buyX(self, buytimes):
        for singlebuy in range(buytimes):
            self.buy()

# If amount is greater than or equal to 1 and plural flag is true, return a
# string for what you have with a plural, else return a string as a singular
# sentence.
    def display(self):
        if (self.amount >= 1):
            print("You have {amount} {name}s".format(
                amount=self.amount, name=self.name))
        else:
            print("You have {amount} {name}".format(
                amount=self.amount, name=self.name))

# Can be called and returns the current cost of the instance.
    def getCost(self):
        return self.cost

# Takes a number as arg and assigns it to the instance as the cost.
    def setCost(self, cost):
        self.cost = cost

# Can be called and returns the current amount of the instance.
    def getAmount(self):
        return self.amount

# Takes a number as arg and assigns it to the instance as the amount.
    def setAmount(self, amount):
        self.amount = amount

# Can be called and returns the current ratio of the instance.
    def getRatio(self):
        return self.ratio

# Takes a number as arg and assigns it to the instance as the ratio.
    def setRatio(self, ratio):
        self.ratio = ratio

# Can be called and returns the flavor text assigned to the instance.
    def getFlavText(self):
        return self.flavText

# Takes a string as arg and assigns it to the instance it's flavor text.
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
