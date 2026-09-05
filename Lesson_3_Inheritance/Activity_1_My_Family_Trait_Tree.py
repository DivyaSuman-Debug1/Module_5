class FamilyMember:
    def __init__(self, eye_color, height_cm):
        self.eye_color = eye_color
        self.height_cm = height_cm

    def show_traits(self):
        print("Eye Color: ", self.eye_color)
        print("Height(cm): ", self.height_cm)

class kid(FamilyMember):
    def __int__(self, name, age, eye_color, height_cm):
        self.name = name
        self.age = age 
        FamilyMember.__init__(eye_color, height_cm)
    def show_traits(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        super().show_traits()

child = kid("Steve", 10, "Black", 200)
child.show_traits()
print("Is a Child a famiymember", issubclass(kid,FamilyMember))