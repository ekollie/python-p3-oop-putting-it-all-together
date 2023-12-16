#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size, condition = "New"):
        self.brand = brand
        self.size = size
        self.condition = condition

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        if int != type(size):
            print("size must be an integer")
        else:
            self._size = size

    # Methods
    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")