from Buyable import Buyable
from Resource import Resource


class Producer(Buyable):

    def __init__(self, name, cost, production, amount=0,
                 ratio=1, flavText=None, multiplier=1):
        super().__init__(name, cost, amount, ratio, flavText)
        self.production = production
        self.multiplier = multiplier

    def produce(self):
        for resource in self.production:
            resource.add(self.production[resource]*self.amount*self.multiplier)

    def update(self):
        self.produce()

    def setMultiplier(self, amount):
        self.multiplier = amount

    def multiply(self, multiplier):
        self.multiplier *= multiplier

    def getProduction(self):
        return self.production

    def setProduction(self, production):
        self.production = production

    def getCurrentProduction(self):
        currentProduction = {}
        for resource in self.production:
            currentProduction[resource] = self.production[resource] * \
                self.multiplier
        return currentProduction

    def getTotalProduction(self):
        totalProduction = {}
        for resource in self.production:
            totalProduction[resource] = self.production[resource] * \
                self.multiplier * self.amount
        return totalProduction


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
