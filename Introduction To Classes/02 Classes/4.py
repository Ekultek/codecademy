"""
Description:

Calling class member variables

Each class object we create has its own set of member variables. Since we've created an object my_car that is an
instance of the Car class, my_car should already have a member variable named condition. This attribute gets assigned
a value as soon as my_car is created.

Challenge:
At the end of your code, use a print statement to display the condition of my_car.
"""
class Car(object):
    condition = "new"

my_car = Car()
print my_car.condition