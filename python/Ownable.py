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
from Modifier import Modifiable

class Ownable(Modifiable):

    def __init__(self, name, amount=0, cap=-1, flavText=None):
        super().__init__()
        self.name = name
        self.amount = amount
        self.flavText = flavText
        self.cap = cap

    # Can be called and returns the current amount of the instance.
    def getAmount(self):
        return self.amount

    # Takes a number as arg and assigns it to the instance as the amount.
    def setAmount(self, amount):
        if self.cap >= 0:
            self.amount = min(amount, self.cap)
        else:
            self.amount = amount

    # Can be called and returns the flavor text assigned to the instance.
    def getFlavText(self):
        return self.flavText

# Takes a string as arg and assigns it to the instance it's flavor text.
    def setFlavText(self, flavText):
        self.flavText = flavText


    def __repr__(self):
        return self.name + " Ownable"