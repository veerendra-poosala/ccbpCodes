#Car_5
# Car class should have the following attributes & methods
#
# Old Attributes:
#   color, max_speed, acceleration, tyre_friction, is_engine_started, current_speed
#
# Old Methods:
#   start_engine, stop_engine, accelerate, apply_brakes
# 
# New Methods:
#   sound_horn:
#       - Print "Beep Beep" if car engine is on
#       - Print "Car has not started yet" if car engine is off
#
# When a new car is created, the engine should be off by default and current_speed should be 0


# Implement the Car class appropriately
class Car:
    def __init__(self, color, max_speed, acceleration, tyre_friction):
        self.color = color
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.tyre_friction = tyre_friction
        self.is_engine_started = False
        self.current_speed = 0
        

    def start_engine(self):
        self.is_engine_started = True
        return self.is_engine_started

    def stop_engine(self):
        self.is_engine_started = False 
        return self.is_engine_started

    def accelerate(self):
        if not self.is_engine_started:
            print("Car has not started yet")
        else:
            self.current_speed += self.acceleration
            if self.current_speed > self.max_speed:
                self.current_speed = self.max_speed

    def apply_brakes(self):
        self.current_speed -= self.tyre_friction
        if self.current_speed < 0:
            self.current_speed = 0

    def sound_horn(self):
        if self.is_engine_started:
            print("Beep Beep")
        else:
            print("Car has not started yet")
            


# You need not change any code below.
# Do not call this function anywhere. It will automatically be called internally during tests.
def default_test():
    car = Car(color="Red", max_speed=250, acceleration=10, tyre_friction=3)
    car.sound_horn()  # Calling the accelerate method when the is_engine_started is False
    car.start_engine()  # Starting the engine
    car.sound_horn()  # Calling the accelerate method when the is_engine_started is True
