print("Supper...!!")

class cmp:
    def parent(self):
        print("This is Parents Mehtod..")

class child(cmp):
    def childd(self):
        print("This is child Method..")
        # super().cmp()

a = child()
a.parent()
