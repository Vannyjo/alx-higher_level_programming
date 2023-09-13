#!/usr/bin/python3
"""Contains a base class called BaseGeometry"""


class BaseGeometry:
    """this defines a class called BaseGeometry"""

    def area(self):
        """method not implemented yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates if a value is an integer
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
