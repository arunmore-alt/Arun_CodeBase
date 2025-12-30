class Emp:
    cmp_name = "Apple"
    NoOfEmp = 0
    def __init__(self, name):
        self.name = name
        self.raise_amt = 0.02
        Emp.NoOfEmp +=1
    def showDetails(self):
        print(f"The Emp Name is {self.name} & The number of emp {self.NoOfEmp} The raise amt is {self.raise_amt} in {self.cmp_name}")

a = Emp("Arun")
a.raise_amt = 0.78
a.cmp_name = "Apple India"
a.showDetails()
# Emp.showDetails(a)
b = Emp("Neha")
b.cmp_name = "Apple Austraila"
b.showDetails()