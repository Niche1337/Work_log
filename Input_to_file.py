import os
import datetime
def clear(self):
    os.system('cls' if os.name == 'nt' else 'clear')

class Add_to_file():
    
    def add_data(self, file):
        data = []
        questions = ["Date of the task\nPlease use the DD/MM/YYYY: ",
                    "Title of the task: ",
                    "Notes (Optional, you can leave this empty): ",]
        print(file)

        clear(self)
        while True:
            try:
                
                q1 = input(questions[0])               
                datetime.datetime.strptime(q1, '%d/%m/%Y') 
                data.append(q1)
                clear(self)
                #raise ValueError("Incorrect data format, should be YYYY/MM/DD")          
                clear(self)
                q2 = input(questions[1])    
                data.append(q2)
                clear(self)
                q3 = input(questions[2])    
                data.append(q3 + "\n")
                break
            except ValueError as err:               
                print("Something went wrong sorry\n{}".format(err))
            



        with open(file, "a") as file:
            file.write(",".join(data))
            
