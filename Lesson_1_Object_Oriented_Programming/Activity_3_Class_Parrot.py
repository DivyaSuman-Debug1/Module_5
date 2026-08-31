class parrot:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Name of Class Parrot: ", self.name)
        print("Age of Class Parrot: ", self.age)
obj=parrot("Kiki", 2)
obj.show()