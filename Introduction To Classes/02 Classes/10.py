"""
Description:

Overriding methods

Since our ElectricCar is a more specialized type of Car, we can give the ElectricCar its own drive_car() method that has
different functionality than the original Car class's.

Challenge:

    1.Inside ElectricCar add a new method drive_car() that changes the car's condition to the string "like new".
    2.Then, outside of ElectricCar, print the condition of my_car
    3.Next, drive my_car by calling the drive_car() function
    4.Finally, print the condition of my_car again
"""
class Car(object):
    condition = "new"

    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

    def display_car(self):
        print "This is a {} {} with {} MPG.".format(self.color, self.model, str(self.mpg))

    def drive_car(self):
        self.condition = "used"


class ElectricCar(Car):
    def __init__(self, battery_type, model, color, mpg):
        self.battery_type = battery_type
        self.model = model
        self.color = color
        self.mpg = mpg

    def drive_car(self):
        self.condition = "like new"


my_car = ElectricCar("molten salt", "cab", "green", 98)
print my_car.condition
my_car.drive_car()
print my_car.condition