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
