# These methods allow you to customize the behavior of your objects in specific contexts,
# making your class instances behave more like built-in types (like integers, lists, etc.).

class Emp:
    def __init__(self,id,name,position,salary):
        self.id=id
        self.name=name
        self.position=position
        self.salary=salary

    def __str__(self):
        return f"{self.id} is {self.name}"

    def __eq__(self, other):         # eq -> 'equal' check's whether the condition is equal
        return self.name==other.name or self.position==other.position

    def __lt__(self, other):        # lt -> 'lesser than'
        return self.salary < other.salary

    def __gt__(self, other):        # gt -> 'greater than'
        return self.salary > other.salary

    def __add__(self, other):
        return self.salary + other.salary

    def __contains__(self, item):
        return item in self.name or item in self.position

    def __getitem__(self, item):
        if item=="name":
            return self.name
        elif item=="position":
            return self.position
        elif item=="salary":
            return self.salary
        else:
            return f"The key '{item}' not found"

    def __len__(self,key):
      return len([self.id,self.name,self.position,self.salary])

e1=Emp(101,"Bob","CEO",45000)
e2=Emp(102,"Alice","Manager",38000)
e3=Emp(103,"John","Developer",30000)
e4=Emp(104,"Bob","Chef",25000)

print(e1)                       # __str__
print(e1.name==e4.name)         # __eq__
print(e2.salary < e3.salary)    # __lt__
print(e2.salary > e4.salary)    # __gt__
print(e1.salary + e3.salary)    # __add__

print("Bob" in e3)              # __contains__
print("Chef" in e4)

print(e1['name'])               # __getitem__
print(e2['salary'])
print(e3['position'])
print(e4['job_description'])

print(len(e3.position))

# Without magic methods,need to create a method like add_vectors(v1, v2) to add vectors manually.
# Magic methods make this seamless.