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

class Resource:

    # Takes a name, amount, amount cap and flag for denoting if you would like
    # plural added to your amount to display sentence. If the cap less than 0,
    # set it to an infinite float, otherwise make it the cap argument.
    def __init__(self, name, amount, cap, plural=False):
        self.name = name
        if cap < 0:
            self.cap = float('inf')
        else:
            self.cap = cap
        self.amount = amount
        self.warning = 0
        self.plural = plural

# Takes amount to add as arg and checks it against the cap, if the amount can
# be added before hitting the cap, add it, otherwise choose cap.
    def add(self, amount):
        self.amount = min(self.cap, self.amount+amount)

# Takes amount to subtract as arg and checks it against current amount, if
# amount to subtract is less than or equal to current amount, subtract it.
# Otherwise, check warning flag for true then make the tick count 20.
    def spend(self, amount, warning=True):
        if amount <= self.amount:
            self.amount -= amount
            return True
        else:
            if warning:
                self.warning = 20
            return False

    def getSpendPercent(self, amount):
        if amount == 0:
            return 1
        return min(1, self.amount/amount)

# Takes an amount as arg and checks if the amount is less than or equal to
# current amount, returns boolean based on evaluation.
    def canAfford(self, amount):
        return amount <= self.amount

# If amount is greater than or equal to 1 and plural flag is true, return a
# string for what you have with a plural, else return a string as a singular
# sentence. If the warning tick is greater than 0, display the warning and
# decrement the warning tick by 1 every update.
    def display(self):
        if (self.amount >= 1 and self.plural):
            print("You have {amount} {name}s".format(
                amount=self.amount, name=self.name))
        else:
            print("You have {amount} {name}".format(
                amount=self.amount, name=self.name))
        if self.warning > 0:
            print("You do not have enough {name}!".format(name=self.name))
            self.warning -= 1

# Can be called and returns the current amount.
    def getAmount(self):
        return self.amount

# Takes an amount as arg and sets the amount to that if it doesn't exceed
# the cap, otherwise it returns the cap.
    def setAmount(self, amount):
        self.amount = min(amount, self.cap)

# Can be called and returns the current set cap for the resource.
    def getCap(self):
        return self.cap

# Takes an amount as arg and if the number is a negative, make the cap
# infinite, otherwise set the arg as the cap.
    def setCap(self, cap):
        if cap < 0:
            self.cap = float('inf')
        else:
            self.cap = cap

# Returns the ratio of current amount over cap.
    def getPercent(self):
        if self.cap == 0:
            return 0
        else:
            return self.amount/self.cap

    def __repr__(self):
        return self.name + " Resource"


if __name__ == "__main__":
    resource = Resource("Wood", 10, 100)
    resource.display()
    resource.add(100)
    resource.display()
