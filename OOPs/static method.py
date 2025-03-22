# static method belongs to class, not to the instance of class
# there is no need to create instance and creating object

class Employee:
    def __init__(self,id,position):
        self.id=id
        self.position=position

    def info(self):
        print(f"{self.id} = {self.position}")

    @staticmethod
    def is_valid_position(position):
        positions=['manager','ceo','cook','developer','cashier']
        return position in positions

emp1=Employee(101,'ceo')
emp2=Employee(102,'manager')
emp3=Employee(103,'cook')
emp1.info()
emp2.info()
emp3.info()

print()
print(Employee.is_valid_position('ceo'))      # directly calling 'Employee' class rather than creating object
print(Employee.is_valid_position('scientist'))