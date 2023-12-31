#!/usr/bin/python3
"""Imports a subclass Rectangle of BaseGeomentry."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square"""

    def __init__(self, size):
        """Initialize a new square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """"returns the area of the square"""
        return self.__size ** 2
