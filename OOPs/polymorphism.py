from abc import ABC,abstractmethod      #ABC -> Abstract Base Class

class Vehicle(ABC):

    @abstractmethod     #decorator to define abstract methods
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car is Starting")

    def stop(self):
        print("Car is Stopping")

class Bike(Vehicle):
    def start(self):
        print("Bike is Starting")

    def stop(self):
        print("Bike is Stopping")

c1=Car()
c1.start()
c1.stop()
print()

b1=Bike()
b1.start()
b1.stop()
