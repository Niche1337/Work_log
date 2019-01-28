import os
import datetime

def clear(self):
    os.system('cls' if os.name == 'nt' else 'clear')

class Search_file():

    def __init__(self, file):
        self.file = file
    
    def search_method(self):
        while True:
            try:
                choices = ["a", "b", "c", "d"]
                choice = input("""
    How would you like to search for the appropirate information.
    a) Find by date?
    b) Find by time spent?
    c) Find by exact search?
    d) Find by pattern?
    Please pick an option.\n""")
                if choice.lower() not in choices:
                    raise ValueError("Enter the valid choices please. a, b or c")
            except ValueError as err:
                print("Unfortunately somthing went wrong sorry.\n{}\nPlease try again".format(err))
            if choice.lower() == "a":
                clear(self)
            elif choice.lower() == "b":
                pass              
            elif choice.lower() == "c":
                pass
            elif choice.lower() == "d":
                pass