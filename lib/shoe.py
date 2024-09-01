#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "New"

        if not isinstance(brand, str):
            raise ValueError("Brand must be a string")
        if not isinstance(size, int):
            raise ValueError("Size must be an integer")
        
         

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value
        if not isinstance(value, str):
            raise ValueError("Brand must be a string")
        

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
        if not isinstance(value, int):
            print("size must be an integer") 
            return
        

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")