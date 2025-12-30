print("Inheritance...")


class Employee:
    def __init__(self,name , id):
        self.name = name
        self.id = id
    
    def showDetails(self):
        print(f"The name of emp is {self.name} and id is {self.id}")
    
class Programmer(Employee):
    def showLanhuge(self):
        print("The Default language is Pyhton ")

class Programmer12(Programmer):
    def showLanhuge12(self):
        print("The Choose language is C++ ")


obj = Employee("Rohan", 546)
obj.showDetails()
obj1 = Programmer("Arun",45)
obj1.showDetails()
obj1.showLanhuge()
obj2 = Programmer12("Neha",34)
obj2.showDetails()
obj2.showLanhuge()
obj2.showLanhuge12()