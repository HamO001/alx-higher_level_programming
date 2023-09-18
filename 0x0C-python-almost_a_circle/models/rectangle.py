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

    def update(self, *args, **kwargs):
        """Update the Rectangle.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
