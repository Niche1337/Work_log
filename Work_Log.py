from Input_to_file import Add_to_file

import os

file = "worklog.csv"
atf = Add_to_file()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def work_log():
    clear()
    print("WORK LOG")
    while True:
        clear()
        try:
            choices = ["a", "b", "c"]
            choice = input("""
    What would you like to do?
    a) Add new entry
    b) Search in existing entries
    c) Quit program\n""")
            if choice.lower() not in choices:
                raise ValueError("Enter the valid choices please. a, b or c")
        except ValueError as err:
            clear()
            print("Unfortunately somthing went wrong sorry.\n{}\nPlease try again".format(err))
            continue
        if choice.lower() == "a":
            clear()
            atf.add_data(file)
        elif choice.lower() == "b":
            pass              
        elif choice.lower() == "c":
            break


if __name__ == "__main__":
    work_log()
