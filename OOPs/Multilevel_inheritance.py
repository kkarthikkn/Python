class Animal:
    def __init__(self,name):
        self.name=name

    def eat(self):
        print(f"{self.name} is eating (Grandparent class)")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking (Parent class)")

class Puppy(Dog):
    def play(self):
        print(f"{self.name} is playing (Child class)")

p1=Puppy("Tommy")

p1.eat()
p1.bark()
p1.play()