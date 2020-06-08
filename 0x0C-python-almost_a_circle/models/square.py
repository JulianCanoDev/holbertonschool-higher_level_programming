#!/usr/bin/python3
"""This is a Square class that heredit from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that heredit from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialization"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get-set the size of the Square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update Square class"""
        pass

    def __str__(self):
        """Return the print() and str()of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
