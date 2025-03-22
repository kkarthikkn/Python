class Bike:
    def __init__(self,brand,model,top_speed,price,color):
        self.brand=brand
        self.model=model
        self.top_speed=top_speed
        self.price=price
        self.color=color

    def drive(self):
        print(f"You can Drive now {self.model}")

    def stop(self):
        print(f"Stop driving bike {self.model}")

    def describe(self):
        print(f"{self.model} is of top_speed {self.top_speed} with the price of ${self.price}"
              f" and the color of {self.color}")