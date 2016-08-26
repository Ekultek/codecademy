# They're multiplying!
class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health = "good"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Add your method here!

    def description(self):
        print self.name
        print self.age


hippo = Animal("Johnny", 25)
hippo.description()
sloth = Animal("Justin", 35)
ocelot = Animal("James", 45)
print sloth.health
print ocelot.health
print hippo.health
