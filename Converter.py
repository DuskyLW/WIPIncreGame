from Producer import Producer
from Resource import Resource


class Converter(Producer):
    def __init__(self, name, cost, production, consumption, enabled=False,
                 amount=0, ratio=1, flavText=None, multiplier=1, efficiency=1):
        super().__init__(name, cost, production, amount,
                         ratio, flavText, multiplier)
        self.consumption = consumption
        self.efficiency = 1
        self.enabled = enabled

    def convert(self):
        for conversion in range(self.amount):
            if self.canConsume():
                self.consume()
                self.produce()
            else:
                break

    def canConsume(self):
        for resource in self.consumption:
            if not resource.canAfford(self.consumption[resource]):
                return False
        return True

    def consume(self):
        currentConsumption = self.getCurrentConsumption()
        for resource in currentConsumption:
            resource.spend(currentConsumption[resource])

    def update(self):
        if self.enabled:
            self.convert()

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getEfficiency(self):
        return self.efficiency

    def setEfficiency(self, efficiency):
        self.efficiency = efficiency

    def getConsumption(self):
        return self.consumption

    def setConsumption(self, consumption):
        self.consumption = consumption

    def getCurrentConsumption(self):
        currentConsumption = {}
        for resource in self.consumption:
            currentConsumption[resource] = self.consumption[resource] / \
                self.efficiency
        return currentConsumption

    def toggle(self):
        if self.enabled:
            self.enabled = False
        else:
            self.enabled = True


if __name__ == "__main__":
    wood = Resource("Wood", 20000, 20000)
    stone = Resource("Stone", 0, 20000)
    converter = Converter("Converter", {wood: 1}, {
                          stone: 10}, {wood: 1}, enabled=True, amount=1)
    print(converter, converter.getAmount())
    print(wood, wood.getAmount())
    print(stone, stone.getAmount())
    converter.update()
    print(converter, converter.getAmount())
    print(wood, wood.getAmount())
    print(stone, stone.getAmount())
    converter.setAmount(10)
    converter.setEfficiency(20)
    converter.update()
    print(converter, converter.getAmount())
    print(wood, wood.getAmount())
    print(stone, stone.getAmount())
