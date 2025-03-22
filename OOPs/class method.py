# Instance Method -> for operations on instance of the class(objects)
# Static method -> for utility functions that do not need access to class data
# Class method -> for class level data or require access to the class itself


class Student:
    count=0
    total_cgpa=0

    def __init__(self,name,cgpa):
        self.name=name
        self.cgpa=cgpa
        Student.count += 1
        Student.total_cgpa+=cgpa

    def info(self):
        print(f"{self.name} = {self.cgpa}")

    @classmethod
    def get_count(cls):
        print(f"Total no of Students: {cls.count}")

    @classmethod
    def avg_cgpa(cls):
        if cls.count==0:
            return 0
        else:
            print(f"Average CGPA: {(cls.total_cgpa/cls.count):.2f}")

s1=Student("Bob",8.5)
s2=Student("Alice",6.3)
s3=Student("John",5.0)
s4=Student("George",7.9)
s1.info()
s2.info()
s3.info()
s4.info()
print()
Student.get_count()
Student.avg_cgpa()