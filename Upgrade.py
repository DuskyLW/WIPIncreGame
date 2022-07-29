from Buyable import Buyable


class Upgrade(Buyable):

    def __init__(self, name, cost, target, effect,
                 amount=0, ratio=1, flavText=None):
        super().__init__(name, cost, amount, ratio, flavText)
        self.target = target
        self.effect = effect

    def buy(self):
        if super().buy():
            # apply the effect to target
            self.effect(self.target)
