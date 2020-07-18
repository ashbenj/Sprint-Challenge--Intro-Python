# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


class Vehicle:
    # Vehicle Class is the base class
    pass


class Flight_Vehicle(Vehicle):

    pass


class Starship(Flight_Vehicle):

    pass


class Airplane(Flight_Vehicle):

    pass


class Ground_Vehicle(Vehicle):

    pass


class Car(Ground_Vehicle):

    pass


class Motorcycle(Ground_Vehicle):

    pass



