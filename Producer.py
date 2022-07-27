from Buyable import Buyable
from Resource import Resource


class Producer(Buyable):

    def __init__(self, resources, cost, amount, resourcetype, resourceamount, name):
        super().__init__(resources, cost, amount)
        self.resourcetype = resourcetype
        self.resourceamount = resourceamount
        self.name = name
        self.mult = 1

    def produce(self):
        for resource in range(len(self.resourcetype)):
            self.resourcetype[resource].add(
                (self.resourceamount[resource])*self.amount*self.mult)

    def setMult(self, amount):
        self.mult = amount

    def display(self):
        if (self.amount >= 1):
            print("You have {amount} {name}s".format(
                amount=self.amount, name=self.name))
        else:
            print("You have {amount} {name}".format(
                amount=self.amount, name=self.name))
