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
            reader = csv.reader(file)
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
                ##Search by date
                x = 1
                try:
                    date_search = input("What is the date you are looking for?\nPlease use the DD/MM/YYYY: ")
                    datetime.datetime.strptime(date_search, '%d/%m/%Y') 
                    for log in self.work_log:
                        if log[3] == "":
                            log[3] = "N/a"
                        if date_search == log[0]:
                            print("{}) Title: {}, Date: {}, Time Spent: {}, Extra Notes: {}".format(x, log[0], log[1], log[2], log[3]))
                            x += 1

                except ValueError as err:               
                    print("Something went wrong sorry\n{}".format(err))
            elif choice.lower() == "b":
                ##search by time spent
                x = 1
                try:
                    task_time = int(input("How long (mins) is the task you are looking for: "))
                    for log in self.work_log:
                        ##needs to be refactored
                        if log[3] == "":
                            log[3] = "N/a"
                        if task_time == int(log[2]):
                            print("{}) Title: {}, Date: {}, Time Spent: {}, Extra Notes: {}".format(x, log[0], log[1], log[2], log[3]))
                            x += 1
                        # elif x == 1:
                        #     print("You entered a invalid number or the task/s with those minutes does not exist.")
                        #     break
                except ValueError:
                    print("Enter a valid number in minutes.")
                if input("Would you like to search again Y/n? ").upper() != "Y":
                    break
            elif choice.lower() == "c":
                ##search by exact name
                x = 1
                exact_term = input("What is the name of the task or details: ").lower()
                for log in self.work_log:
                    if log[3] == "":
                        log[3] = "N/a"
                    if exact_term in log[1].lower() or exact_term in log[3].lower():
                        print("{}) Title: {}, Date: {}, Time Spent: {}, Extra Notes: {}".format(x, log[0], log[1], log[2], log[3]))
                        x += 1
                    # elif x == 1:
                    #     print("You entered an incorrect term or it does not exist")
                    #     continue
                if input("Would you like to search again Y/n? ").upper() != "Y":
                    break
            elif choice.lower() == "d":
                ##search by regEx
                break
