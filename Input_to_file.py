import os
def clear(self):
    os.system('cls' if os.name == 'nt' else 'clear')

class Add_to_file():
    def __init__(self):
        print("Hello")


    
    def add_data(self, file):
        data = []
        questions = ["Date of the task\nPlease use the DD/MM/YYYY: ",
                    "Title of the task: ",
                    "Notes (Optional, you can leave this empty): ",]
        print(file)
        clear(self)
        data.append(input(questions[0]))
        clear(self)
        data.append(input(questions[1]))
        clear(self)
        data.append(input(questions[2]))

