import os
import datetime
import csv

def clear(self):
    os.system('cls' if os.name == 'nt' else 'clear')

class Search_file():

    def __init__(self, file):
        self.file = file
        self.work_log = []
        with open(self.file, newline = '') as file:
            reader = csv.DictReader(file)
            self.work_log = list(reader)     
    
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
                    raise ValueError("Enter the valid choices please, a, b, c or d")
            except ValueError as err:
                print("Unfortunately somthing went wrong sorry.\n{}\nPlease try again".format(err))
            if choice.lower() == "a":
                print(self.work_log)
            elif choice.lower() == "b":
                break              
            elif choice.lower() == "c":
                break
            elif choice.lower() == "d":
                break
