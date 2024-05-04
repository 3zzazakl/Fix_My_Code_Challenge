#!/usr/bin/python3
"""Square class"""


class Square():
    """Square class"""

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Initialize a new square"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """Return the area of the square"""
        return self.width * self.height

    def permiter_of_my_square(self):
        """Return the perimeter of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Return the square dimensions"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """Main"""

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
