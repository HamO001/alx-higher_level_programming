#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Rectangle class, inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor."""
        super().__init__(id)
        self.width = width  # Validate and set the width attribute
        self.height = height  # Validate and set the height attribute
        self.x = x  # Validate and set the x attribute
        self.y = y  # Validate and set the y attribute

    @property
    def width(self):
        """Getter for width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width attribute with validation."""
        if not isinstance(value, int):
            raise TypeError(
                    "width must be an integer"  # Check if it's an integer
                    )
        if value <= 0:
            raise ValueError(
                    "width must be > 0"  # Check if it's greater than 0
                    )
        self.__width = value  # Set the width attribute

    @property
    def height(self):
        """Getter for height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height attribute with validation."""
        if not isinstance(value, int):
            raise TypeError(
                    "height must be an integer"  # Check if it's an integer
                    )
        if value <= 0:
            raise ValueError(
                    "height must be > 0"  # Check if it's greater than 0
                    )
        self.__height = value  # Set the height attribute

    @property
    def x(self):
        """Getter for x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x attribute with validation."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")  # Check if it's an integer
        if value < 0:
            raise ValueError(
                    "x must be >= 0"
                    # Check if it's greater than or equal to 0
                    )
        self.__x = value  # Set the x attribute

    @property
    def y(self):
        """Getter for y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y attribute with validation."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")  # Check if it's an integer
        if value < 0:
            raise ValueError(
                    "y must be >= 0"
                    # Check if it's greater than or equal to 0
                    )
        self.__y = value  # Set the y attribute

    def area(self):
        """calculate and return the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """display the rectangle using the # character to stdout"""
        for _ in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        """Override the __str__ method to return formatted string."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
