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

class Modifier():

    def __init__(self, function, items=None) -> None:
        self.function = function
        self.items = items


    def value(self):
        return self.function(self.items)

class Modifiable():

    def __init__(self) -> None:
        self.modifiers = {}
        self.labels = []
        
    def addModifier(self, modifier, label):
        if  label in self.modifiers:
            self.modifiers[label].append(modifier)
        else:
            self.modifiers[label] = [modifier]

    def clearModifiers(self):
        self.modifers = {}

    def getModifers(self, label):
        return [modifier.value() for modifier in self.modifiers[label]]


if __name__=="__main__":
    modifiable  = Modifiable()
    mult1 = Modifier(lambda items: 5)
    mult2 = Modifier(lambda items: 6)
    modifiable.addModifier(mult1, "linear")
    modifiable.addModifier(mult2, "linear")
    print(modifiable.getModifers("linear"))