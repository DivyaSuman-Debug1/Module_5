class Myclass:
    __privateVar = 27
    def __privateVar(self):
        print("I'm inside My Class")
    def hello(self):
        print("The Private Variable :", Myclass.__privateVar)
foo = Myclass()
foo.hello()
foo.__privateVar()