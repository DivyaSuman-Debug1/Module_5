class student:
    sname = "Student1"
    sno = 12

    def __init__(self):
        print("I am a Student")

    def show(self):
        print(self.sname, self.sno)
obj=student()
obj.show()