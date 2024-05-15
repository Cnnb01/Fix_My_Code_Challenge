#!/usr/bin/python3
"""A square"""


class Square():
    """defining a square"""

    __width = 0
    __height = 0

    def __init__(self, width=0, height=0):
        """Initializing class square"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width attriute"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
        else:
            raise TypeError("height must be an integer")

    def area_of_my_square(self):
        """ Area of the square """
        return self.__width * self.__height

    def perimeter_of_my_square(self):
        """Perimeter of the square"""
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """String representation of the class square"""
        return "{}/{}".format(self.__width, self.__height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
