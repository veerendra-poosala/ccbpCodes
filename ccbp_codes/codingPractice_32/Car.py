#Car

# Car class should have the following attributes & methods
#
# Attributes:
#   color, max_speed, acceleration, tyre_friction
#


# Implement the Car class appropriately
class Car:
    def __init__(self,color,max_speed,acceleration,tyre_friction):
        self.color = color
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.tyre_friction = tyre_friction


# You need not change any code below.
# Do not call this function anywhere. It will automatically be called internally during tests.
def default_test():
    car = Car(color="Red", max_speed=250, acceleration=10, tyre_friction=3)
    print(car.color)
    print(car.max_speed)
    print(car.acceleration)
    print(car.tyre_friction)
