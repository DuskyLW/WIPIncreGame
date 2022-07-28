from Buyable import Buyable
from Resource import Resource


class Converter(Buyable):
    def __init__(self, resources, cost, amount, convertresource, convertresourceamount, name, outputresource, outputamount):
        super().__init__(resources, cost, amount)
        self.convertresource = convertresource
        self.convertresourceamount = convertresourceamount
        self.name = name
        self.converting = False
        self.outputresource = outputresource
        self.outputamount = outputamount

    def convert(self):
        if self.converting and self.canconvert():
            for resource in range(len(self.convertresource)):
                self.convertresource[resource].spend((self.convertresourceamount[resource]), False)
            for outputresource in range(len(self.outputresource)):
                self.outputresource[outputresource].add(self.outputamount[outputresource])

    def canconvert(self):
        for resource in range(len(self.convertresource)):
            if not self.convertresource[resource].canafford(self.convertresourceamount[resource]):
                return False
        return True

    def updatename(self, name):
        self.name = name

    def updateresource(self, convertresource):
        self.convertresource = convertresource

    def updateresourceamount(self, convertresourceamount):
        self.convertresourceamount = convertresourceamount

    def updateoutputresource(self, outputresource):
        self.outputresource = outputresource

    def updateoutputamount(self, outputamount):
        self.outputamount = outputamount

    def toggle(self):
        if self.converting:
            self.converting = False
        else:
            self.converting = True

    def display(self):
        if (self.amount >= 1):
            print("You have {amount} {name}s".format(amount=self.amount, name=self.name))
        else:
            print("You have {amount} {name}".format(amount=self.amount, name=self.name))
