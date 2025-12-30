print("Decorater....!!")


def greet(fx):
    def mfx():
        print("Good Morning..!!")
        fx()
        print("Thank u using this Function...")
    return mfx


@greet
def hell():
    print("Hello..!!, Arun")

hell()

