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

    def __init__(self, name, cost, target, effect,
                 amount=0, cap=1, ratio=1, flavText=None):
        super().__init__(name, cost, amount, cap=cap, ratio=ratio, flavText=flavText)
        self.target = target
        self.effect = effect

    def buy(self):
        if super().buy():
            # apply the effect to target
            self.effect(self.target)
