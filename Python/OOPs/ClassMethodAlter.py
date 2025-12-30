print("Class Methods Alternative....!!!")

class Emp:
    def __init__(self, Name , salary):
        self.name = Name
        self.salary = salary
    @classmethod
    def fromStr(cls,str):
        return cls(str.split("-")[0], int(str.split("-")[1]))

e1 = Emp("Arun", 20000)
print(e1.name)
print(e1.salary)

str = "John-120000"
e2 = Emp.fromStr(str)
print(e2.name)
print(e2.salary)
