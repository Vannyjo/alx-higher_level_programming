#!/usr/bin/python3
"""Declearing the class Square"""
class Square:
    def __init__(self, size = 0):

        """ set the private instance attribute '_size'"""
        self._size = size

        try

        """ First, check if 'size' is an integer"""
        if not isinstance(size, int):

            except TypeError:
                print("size must be an integer")

         """ Next, check if 'size' is less than 0"""
        if size < 0:
            except ValueError:
                print("size must be >= 0")


