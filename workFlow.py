#Imports
import pickle
import os

class TaskHandler:
    def __init__(self):
        
        self.storagefn = 'taskStorage.pkl' # Filename of storage

        self.tasks = []
        f = openStorageFile(self.storagefn,"rb")
        with f:
            while True:
                try:
                    self.tasks.append(pickle.load(f))
                except:
                    #No more objects in file
                    break


    def dumpAll(self):
        #Saves all objects in pickle file
        f = openStorageFile(self.storagefn,"wb")
        with f:
            #Deletes all contents in file
            pass
        
        f = openStorageFile(self.storagefn,"wb")
        with f:
            for task in self.tasks:
                pickle.dump(task,f)
       
   

class Task:
    def __init__(self,taskType):
        self.taskType = taskType
        self.steps = loadTaskSteps(self.taskType)
        self.spos = 0
        self.getNextSteps()
        self.description = input("Please write a short description to dsiplay for furture users:")

    def getNextSteps(self):
        #Gets the next possible steps in the work flow
    
        self.nextSteps = []
        for rel in self.steps[self.spos].nextStepsRel:
            self.nextSteps.append(self.steps[self.spos+rel])

    def navigateWf(self):
        print("The current work flow step is:",self.steps[self.spos].stepName)    


class Step:
    def __init__(self,stepName,nextStepsRel = []):
        self.stepName = stepName
        self.nextStepsRel = nextStepsRel




def loadTaskSteps(taskType):
    return [Step("Update FMA Schedule",[1]),
            Step("Create ammendment letter",[1]),
            Step("Review FMA",[-2,1]),
            Step("Review Ammendment Letter",[-2,1]),
            Step("Send FMA documents to Leeds",[1]),
            Step("Save documents")
            ]


def startNewTask(handler):
    print("-----------")
    print("Select one of the below to create it as a task")
    print("1: FMA Update")
    print("2: Exit back to main menu")
    print("--------------")

    choice = getChoice(2)
    if choice != 2:
        if choice == 1:
            taskType = "FMA Update"

        
        newTask = Task(taskType)
        handler.tasks.append(newTask)

def openStorageFile(fn,openType):
    """
    Opens a file.

    fn(str) -> Target file to open 
    openType(str) - > type of open to go in open function
    
    """
    error = False
    while True:
            try:
                if not error:
                    f = open(f'{os.getcwd()}\\{fn}',openType)
                elif error:
                    f = open(f'{path}',openType) 
            except FileNotFoundError:
                error = True
                print("Could not find the storage file")
                path = input("Please enter the file path to find storage file:")
            
            break
    
    return f

def viewTasks(handler):
    

    for i in range(len(handler.tasks)):
        print(f'{i+1}) {handler.tasks[i].taskType} - {handler.tasks[i].description}')

    

def main():
    #main function
    print("Code Started")
    handler = TaskHandler()
    while True:
        #Main loop

        #Main menu
        choice = menu()
        if choice == 3:
            #Write code here for saving the existing objects
            print("Closing the code")
            handler.dumpAll()
            exit()
        elif choice == 1:
            startNewTask(handler)
        
        elif choice == 2:
            viewTasks(handler)

def getChoice(maxChoice):
    #Error catching
    try:
        choice = int(input("Please enter an option:"))
    except ValueError:
        print("You did not enter a number. Can you try again please")

    if choice not in range(1,maxChoice+1):
        print("You did not enter a valid number. Can you try again please")

    return choice      

def menu():
    print("----------------")
    print("1: Start new task")
    print("2: View tasks")
    print("3: Exit the code")
    print("----------------")

    return getChoice(3)
        

if __name__ == "__main__":
    os.chdir(r"C:\Users\millso\OneDrive - TPT Retirement Solutions\Desktop\CodeQuick\Dev\workFlow")
    main()
