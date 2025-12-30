print("Static..")

class Math:
    def __init__(self, num):
        self.num = num
    
    def add(self, a):
        return self.num + a
    
    def addTwo(self,b , c):
        return b+c

a = Math(6)
print(a.num)
print(a.add(5))
print(a.addTwo(4,3))
