class Vehicle:
    def move(self):
        print("Vehicle is moving.")

class Car(Vehicle):
    def move(self):
        print("Car is moving on road.")

class Bike(Vehicle):
    def move(self):
        print("Bike is moving on track.")

# Example usage:
vehicle = Vehicle()
vehicle.move()  # Output: Vehicle is moving.

car = Car()
car.move()  # Output: Car is moving on road.

bike = Bike()
bike.move()  # Output: Bike is moving on track.
