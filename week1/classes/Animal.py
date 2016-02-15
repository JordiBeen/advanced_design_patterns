class Animal():
    def Eat(self):
        print('Eating')

    def Move(self):
        print('Moving')

    def GetName(self):
        print(self._name)

    def SetName(self, name):
        self._name = name
