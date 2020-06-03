#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry():
    """BaseGeometry class"""
    def area(self):
        """Area of BaseGeometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Integer validator"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(value))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(value))


class Rectangle(BaseGeometry):
    """Heredit from BaseGeometry class"""
    def __init__(self, width, height):
        """Initialization"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
