class Father:
    def skill(self):
        print("Swimming,Running(F)")

class Mother:
    def skill(self):
        print("Cooking,Arts(M)")

class Child(Father,Mother):
    def skill(self):
        Father.skill(self)      #if the parent class has same method then need to do explicit method call
        Mother.skill(self)
        print("Dance(C)")

c1=Child()
c1.skill()
print()
print(Child.mro())  # MRO -> Method Order Resolution