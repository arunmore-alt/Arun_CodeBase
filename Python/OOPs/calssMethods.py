print("Class Methods..")


class Empp:
    company ="Apple"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")
    @classmethod
    def changeCmp(cls, newcmp):
        cls.company= newcmp
    
e1 = Empp()
e1.name = "Arun"
e1.show()
e1.changeCmp("Tesla")
e1.show()
print(Empp.company)