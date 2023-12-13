#!/usr/bin/env python3

class Book:
    
    def __init__(self, page_count = -1 , title = "Default"):
        self.page_count = page_count
        self.title = title

    def get_page_count(self):
        print("Getting page count")
        print(self._page_count)
        
    def set_page_count(self, page_count):
        if(isinstance(page_count, int)):
            self._page_count = page_count
        else: print("page_count must be an integer")

    def get_title(self):
        print("Getting title")
        return self._title
        
    def set_title(self, title):
        if(isinstance(title, str)):
            self._title = title
        else: print("not a string")
        
    def turn_page():
        print("Flipping the page...wow, you read fast!")


    page_count = property(get_page_count, set_page_count)
    title = property(get_title, set_title)
