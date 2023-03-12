"""
In Python, dunder methods are methods that allow instances of a class to interact
with the built-in functions and operators of the language. The word “dunder” comes
from “double underscore”, because the names of dunder methods start and end with two
underscores, for example __str__ or __add__. Other names are Python Magic Functions
"""


class Vector:
    def __init__(self, x, y):
        """ Dunder initializer """
        self.x = x
        self.y = y

    def __add__(self, other):
        """ Dunder operator overloading - oop """
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        """ Dunder string representation  """
        return f"vector.x = {self.x} vector.y = {self.y}"

    def __del__(self):
        print("Vector object is deleted")


def main():
    v1 = Vector(1, 2)
    v2 = Vector(4, 9)
    v = v1 + v2
    print(v)


if __name__ == '__main__':
    main()
