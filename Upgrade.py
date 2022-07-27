from Buyable import Buyable


class Upgrade(Buyable):

    def __init__(self, resources, cost, amount, target, effect, name):
        super().__init__(resources, cost, amount)
        self.target = target
        self.effect = effect
        self.name = name

    def buy(self):
        if super().buy():
            # apply the effect to target
            self.effect(self.target)
