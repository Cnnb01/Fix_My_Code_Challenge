#!/usr/bin/python3
"""A square"""


class Square():
    """defining a square"""

    def __init__(self, width=0):
        """Initializing class square"""
        self.__width = width

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width attribute"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        else:
            raise TypeError("width must be an integer")

    def area_of_my_square(self):
        """ Area of the square """
        return self.__width * self.__width

    def perimeter_of_my_square(self):
        """Perimeter of the square"""
        return (self.__width * 4)

    def __str__(self):
        """String representation of the class square"""
        return "{}/{}".format(self.__width, self.__width)


if __name__ == "__main__":

    s = Square(width=12)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())

