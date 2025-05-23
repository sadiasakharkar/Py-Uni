# super() = function used to give access to the methods of a parent class .
#           Returns a temporary object of a parent class when used

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)  # Only one argument needed since it's a square

    def area(self):
        return self.length * self.width

class Cube(Rectangle):
    def __init__(self, length, height):
        super().__init__(length, length)  # Only length needed for both length and width
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

square = Square(3)
cube = Cube(3, 3)

print(square.area())  # Output: 9
print(cube.volume())  # Output: 27
