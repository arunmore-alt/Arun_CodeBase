x = [1,2,3]
print(dir(x))
print(x.__add__)


b = (1,2,3)
print(dir(b))
# print(b.__add__)

class emp:
    def __init__(self,name,age):
        self.name=name
        self.age = age
    
p = emp("Arun",23)
print(p.__dict__)
print(help(emp))