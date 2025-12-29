print("Constructer..!!")

class Person:
    # name = "Arun"
    # JR = "Software Developer"
    
    # networth = 23

    def __init__(self, n , j):
        print("Hy I am a construter...")
        self.name = n
        self.Job = j
    def info(self):
        print(f"The name is {self.name} and Job is a {self.Job}")

a = Person("Arun", "Developer")
b = Person("Neha", "Hr")


a.info()
b.info()