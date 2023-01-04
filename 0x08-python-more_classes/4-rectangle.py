#!/usr/bin/python3
"""Class defines a rectangle."""


class Rectangle:
    """Define a Rectangle."""
    def __init__(self, width=0, height=0):
        """Initialize a Rectangle.

        Args:
            width(int): Width of the new Rectangle
            height(int): Height of the new Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter that returns the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method that sets the width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method to return height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of a rectangle."""
        return self.__height * self.__width

    def perimeter(self):
        """Return the perimeter of a rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Prints the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = []

        for i in range(self.__height):
            for j in range(self.__width):
                rect.append('#')
            if i != self.__height - 1:
                rect.append('\n')
        return "".join(rect)

    def __repr__(self):
        """Returns string representation of the rectangle."""
        return "Rectangle({}, {})".format(self.__width, self.__height)
