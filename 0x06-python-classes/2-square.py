#!/usr/bin/python3

"""Define Class Square"""


class Square:
    """Class Square."""

    def __init__(self, size=0):
        """Initialize new square.
        Args:
            size (int):Size ofnew square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
