#!/usr/bin/python3
"""A square with a size."""


class Square:
    """Define the square."""
    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
