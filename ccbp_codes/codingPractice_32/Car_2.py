#Car_2
# Car class should have the following attributes & methods
# 
# Old Attributes: 
#   color, max_speed, acceleration, tyre_friction
# New Attributes:
#   is_engine_started
# 
# Methods:
#   start_engine: When this method is called, should set the value of attribute is_engine_started to True 
# which indicates that the car engine is turned on
# 
#   stop_engine: When this method is called, should set the value of attribute is_engine_started to False
# which indicates that car engine is turned off
# 
# When a new car is created, the engine should be off by default


# Implement the Car class appropriately
class Car:
    def __init__(self, color, max_speed, acceleration, tyre_friction,is_engine_started = False):
        self.color = color
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.tyre_friction = tyre_friction
        self.is_engine_started = is_engine_started

    def start_engine(self):
        self.is_engine_started = True
        return self.is_engine_started

    def stop_engine(self):
        self.is_engine_started = False
        return self.is_engine_started


# You need not change any code below.
# Do not call this function anywhere. It will automatically be called internally during tests.
def default_test():
    car = Car(color="Red", max_speed=250, acceleration=10, tyre_friction=3)
    print(car.is_engine_started)  # As car is not yet started, it should print False
    car.start_engine()  # Starting the engine
    print(car.is_engine_started)  # As engine is on, it should print True
    car.stop_engine()  # Stopping the engine
    print(car.is_engine_started)  # As engine is off, it should print False
