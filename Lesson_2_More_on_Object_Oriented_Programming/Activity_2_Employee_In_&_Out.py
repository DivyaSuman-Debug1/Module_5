class Employee:
    def __init__(self):
        print("Employee is Here")
    def __del__(self):
        print("Destructur has been Called")

def create_obj():
    print("Making Objects")
    obj = Employee()
    return obj

print(create_obj())