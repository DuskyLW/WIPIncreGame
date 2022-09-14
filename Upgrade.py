#   Written by Dallin Dmytryk, Charlie Yeudall 2022
#
#    Copyright 2022 Dallin Dmytryk, Charlie Yeudall
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from Buyable import Buyable


class Upgrade(Buyable):

    # Takes a name for the upgrade object, cost to buy, the target to upgrade,
    # the effect of the upgrade, the amount that has already been
    # bought/ current iteration of amount of times bought, a ratio that
    # describes how much extra each new upgrade will cost, and a flavor text
    # for the object.
    def __init__(self, name, cost, target, effect,
                 amount=0, ratio=1, flavText=None):
        # The super().__init__ allows for access to the methods of
        # Buyable from within Upgrade.
        super().__init__(name, cost, amount, ratio, flavText)
        self.target = target
        self.effect = effect

# Based on the method from Buyable, if the upgrade is affordable, it is bought
# follow by the effect of the upgrade applying to the target to upgrade.
    def buy(self):
        if super().buy():
            # Apply the effect to target
            self.effect(self.target)
