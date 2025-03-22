# class Child(Parent):

class SmartPhone:
    def __init__(self,brand):
        self.brand=brand

    def videocall(self):
        print(f"{self.brand} allows video call")

    def selfie(self):
        print(f"{self.brand} allows selfie")

    def network(self):
        print(f"{self.brand} allows 4G")


class Oppo(SmartPhone):
    def battery(self):
        print("Oppo A52 has 5000 mah battery")

class Vivo(SmartPhone):
    pass

sp1=Oppo("Oppo A52")            # Create an Oppo instance, which has the 'battery' method
sp2=Vivo("Vivo Y13")      # Create a SmartPhone instance (no 'battery' method)

sp1.videocall()
sp1.selfie()
sp1.network()
sp1.battery()
print()
sp2.videocall()
sp2.selfie()
sp2.network()


