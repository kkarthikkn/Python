class animal:
    def __init__(self,name):
        self.name=name
        self.is_alive=True

    def eat(self):
        print(f"{self.name} can eat")

    def sleep(self):
        print(f"{self.name} can sleep")

class dogs(animal):
    def sound(self):
        print(f"{self.name} barks")

class cats(animal):
    def sound(self):
        print(f"{self.name} meows")

    def sleep(self):
        print(f"{self.name} is awake")      # Overriding the sleep method for cats

dg=dogs("Tommy")
ct=cats("Kitty")

dg.eat()
dg.sleep()
dg.sound()
print()
ct.eat()
ct.sleep()
ct.sound()