"""
Description:

Inheritance

One of the benefits of classes is that we can create more complicated classes that inherit variables or methods from
their parent classes. This saves us time and helps us build more complicated objects, since these child classes can
also include additional variables or methods.

We define a "child" class that inherits all of the variables and functions from its "parent" class like so:

class ChildClass(ParentClass):
    # new variables and functions go here

Normally we use object as the parent class because it is the most basic type of class, but by specifying a different
class, we can inherit more complicated functionality.

Challenge:
Create a class ElectricCar that inherits from Car. Give your new class an __init__() method of that includes a
"battery_type" member variable in addition to the model, color and mpg.

Then, create an electric car named "my_car" with a "molten salt" battery_type. Supply values of your choice for the
other three inputs (model, color and mpg).
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


my_car = ElectricCar("molten salt", "cab", "green", 98)
