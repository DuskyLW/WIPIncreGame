from Buyable import Buyable
from Resource import Resource


class Producer(Buyable):

    def __init__(self, resources, cost, amount, resourcetype, resourceamount, name):
        super().__init__(resources, cost, amount)
        self.resourcetype = resourcetype
        self.resourceamount = resourceamount
        self.name = name
        self.multiplier = 1

    def produce(self):
        for resource in range(len(self.resourcetype)):
            self.resourcetype[resource].add(
                (self.resourceamount[resource])*self.amount*self.multiplier)

    def setMultiplier(self, amount):
        self.multiplier = amount

    def multiply(self, multiplier):
        self.multiplier *= multiplier

    def updatename(self, name):
        self.name = name

    def updateresource(self, resourcetype):
        self.resourcetype = resourcetype

    def display(self):
        if (self.amount >= 1):
            print("You have {amount} {name}s".format(
                amount=self.amount, name=self.name))
        else:
            print("You have {amount} {name}".format(
                amount=self.amount, name=self.name))


if __name__ == "__main__":
    wood = Resource("Wood", 20000, 20000)
    producer = Producer([wood], [20], 1, [wood], [1], "Worker")
    producer.multiply(100)
