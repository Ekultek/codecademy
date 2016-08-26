"""
Description:

Referring to member variables

Calling class member variables works the same whether those values are created within the class
(like our car's condition) or values are passed into the new object at initialization. We use dot notation to access
the member variables of classes since those variables belong to the object.

For instance, if we had created a member variable named new_variable, a new instance of the class named new_object could
access this variable by saying:

new_object.new_variable

Challenge:
Now that you've created my_car print its member variables:

    First print the model of my_car. Click "Stuck? Get a hint!" for an example.
    Then print out the color of my_car.
    Then print out the mpg of my_car.
Now that you've created my_car print its member variables:

    1.First print the model of my_car. Click "Stuck? Get a hint!" for an example.
    2.Then print out the color of my_car.
    Then print out the mpg of my_car.
"""


class Car(object):
    condition = "new"

    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg


my_car = Car("DeLorean", "silver", 88)
print my_car.condition
print my_car.model
print my_car.color
print my_car.mpg
