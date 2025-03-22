class Student:
    batch=2025          # batch & present are class_var ie common for all objects
    present=0

    def __init__(self,name,age):
        self.name=name
        self.age=age            # instance_variable
        Student.present+=1      # should not use 'self.' bcz its class_var not instance_var

st1=Student("Bob",24)
st2=Student("Alice",25)
st3=Student("John",23)

print(f"There are {Student.present} students of {Student.batch} batch. Students are:\n ")

print(f"{st1.name}'s age is {st1.age}")
print(f"{st2.name}'s age is {st2.age}")
print(f"{st3.name}'s age is {st3.age}")


#print(st1.name)
#print(st1.age)
#print(st2.name)
#print(st2.age)

#print(Student.batch)   #using 'Student.' bcz of class_var, it's common for every created obj
#print(Student.present)

