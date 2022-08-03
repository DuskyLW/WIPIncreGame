class Resource:

    def __init__(self, name, amount, cap, plural=False):
        self.name = name
        if cap < 0:
            self.cap = float('inf')
        else:
            self.cap = cap
        self.amount = amount
        self.warning = 0
        self.plural = plural

    def add(self, amount):
        self.amount = min(self.cap, self.amount+amount)

    def spend(self, amount, warning=True):
        if amount <= self.amount:
            self.amount -= amount
            return True
        else:
            if warning:
                self.warning = 20
            return False

    def canAfford(self, amount):
        return amount <= self.amount

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

    def getAmount(self):
        return self.amount

    def setAmount(self, amount):
        self.amount = min(amount, self.cap)

    def getCap(self):
        return self.cap

    def setCap(self, cap):
        if cap < 0:
            self.cap = float('inf')
        else:
            self.cap = cap

    def getPercent(self):
        if self.cap <= 0:
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
