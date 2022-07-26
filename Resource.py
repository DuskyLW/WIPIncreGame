class Resource:

    def __init__(self, name, cap, amount, plural=False):
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

    def spend(self, amount):
        if amount <= self.amount:
            self.amount -= amount
            return True
        else:
            self.warning = 20
            return False

    def display(self):
        if (self.amount >= 1 and self.plural):
            print("You have {amount} {name}s".format(amount=self.amount, name=self.name))
        else:
            print("You have {amount} {name}".format(amount=self.amount, name=self.name))
        if self.warning > 0:
            print("You do not have enough {name}!".format(name=self.name))
            self.warning -= 1


if __name__ == "__main__":
    resource = Resource("Wood", 100, 10)
    resource.display()
    resource.add(100)
    resource.display()
