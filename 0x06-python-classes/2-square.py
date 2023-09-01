#!/usr/bin/python3


"""Module for defining a Square class."""

class Square:

    """A class that defines a square.

    Attributes:
        _size (int): The size of the square.
    """

    def __init__(self, size=0):

        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square. Default is 0.

        Raises:
            TypeError: If `size` is not an integer.
            ValueError: If `size` is less than 0.
        """

        if not isinstance(size, int):

            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self._size = size

