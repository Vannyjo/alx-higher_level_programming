#!/usr/bin/python3
"""defines a base class"""

class base:

    """initializing the class private attribute"""
    __nb_objects = 0

    """defining the base class args, and variables"""
    def __init__(self, id=None):

        """Initialize a new Base.
        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
