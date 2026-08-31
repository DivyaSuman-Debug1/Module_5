class vehicle:
    def __init__(self, max_speed, milage):
        self.max_speed = max_speed
        self.milage = milage

    def show(self):
        print("Speed of Vehicle: ", self.max_speed) 
        print("Milage of Vehicle: :", self.milage)
obj=vehicle(50, 25)
obj.show()