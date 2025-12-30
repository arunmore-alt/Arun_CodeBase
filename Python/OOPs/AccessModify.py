print("Access Modify...")

class Employee:
    def __init__(self):
        self.name = "Arun"
        self.id = 45
        self.__subject = "C++" # Privater Members

a = Employee()
# By Default all members are Public
print(a.name)
print(a.id)
print(a._Employee__subject)
# print(a.__dir__())
