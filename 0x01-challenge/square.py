#!/usr/bin/python3
"""A square"""


class square():
    """defining a square"""

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Initializing class square"""
        for key, value in kwargs.items():
            setattr(self, key, value)

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
        return self.width * self.height

    def PermiterOfMySquare(self):
        """Perimeter of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """String representation of the class square"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
