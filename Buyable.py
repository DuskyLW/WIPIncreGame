from Resource import Resource


class Buyable:

    def __init__(self, resources, cost, amount):
        self.resources = resources
        self.cost = cost
        self.amount = amount

    def canbuy(self):
        for resource in range(len(self.resources)):
            if self.resources[resource].amount >= self.cost[resource]:
                pass
            else:
                return False
        return True

    def buy(self):
        if self.canbuy():
            for resource in range(len(self.resources)):
                self.resources[resource].spend(self.cost[resource])
            self.amount += 1
            return True
        return False

    def updatecostresources(self, resources):
        self.resources = resources

    def updatecost(self, cost):
        self.cost = cost

    def buyalot(self, buytimes):
        for singlebuy in range(buytimes):
            self.buy()


if __name__ == "__main__":
    wood = Resource("Wood", 20000, 20000)
    buyable = Buyable([wood], [20], 0)
    buyable.buyalot(1000)
    print(buyable.amount)
