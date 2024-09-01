#!/usr/bin/env python3

class Book:
     def __init__(self, title, page_count):
        self.title = title
        self._page_count = page_count 

        if not isinstance(title, str):
            raise ValueError("Title must be a string")
        if not isinstance(page_count, int):
            raise ValueError("page_count must be an integer")

     @property
     def page_count(self):
        return self._page_count

     @page_count.setter
     def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
            return
        self._page_count = value

     def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    
        