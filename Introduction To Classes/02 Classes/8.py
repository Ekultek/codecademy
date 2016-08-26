"""
Description:

Modifying member variables

We can modify variables that belong to a class the same way that we initialize those member variables. This can be
useful when we want to change the value a variable takes on based on something that happens inside of a class method.

Challenge:


    1.Inside the Car class, add a method drive_car() that sets self.condition to the string "used".
    2.Remove the call to my_car.display_car() and instead print only the condition of your car.
    3.Then drive your car by calling the drive_car() method.
    4.Finally, print the condition of your car again to see how its value changes.
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


my_car = Car("DeLorean", "silver", 88)
print my_car.condition
print my_car.drive_car()
print my_car.condition
