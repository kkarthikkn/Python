class Wild:
    def __init__(self,name):
        self.name=name
    def carn(self):
        print(f"{self.name} is carnivorous")

class Domestic:
    def __init__(self,name):
        self.name=name
    def herb(self):
        print(f"{self.name} is herbivorous")

class Human(Wild,Domestic):
    def __init__(self,name):
        Wild.__init__(self,name)
        Domestic.__init__(self,name)

    def omni(self):
        print(f"{self.name} is Omnivorous")

w1=Wild("Lion")
d1=Domestic("Cow")
h1=Human("Alice")

w1.carn()
d1.herb()
h1.herb()
h1.carn()
h1.omni()

print(Human.mro())  # MRO -> Method Order Resolution