#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size) -> None:
        self.brand = brand
        if isinstance(size, int):
            self.size = size
        else:
            print("size must be an integer")

    @property
    def size(self):
        return self._size

    @size.getter
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")

    def cobble(self):
        self.condition = 'New'
        print("Your shoe is as good as new!")
        return
