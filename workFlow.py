#Imports
import pickle


class Task:
    def __init__(self,taskType):
        self.taskType = taskType
        self.steps = loadTaskSteps(self.taskType)
        self.spos = 0
        self.getNextSteps()

    def getNextSteps(self):
        #Gets the next possible steps in the work flow
    
        self.nextSteps = []
        for rel in self.steps[self.spos].nextStepsRel:
            self.nextSteps.append(self.steps[self.pos+rel])

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


def startNewTask():
    print("-----------")
    print("Select one of the below to create it as a task")
    print("1: FMA Update")
    print("2: Exit back to main menu")
    print("--------------")

    choice = getChoice(2)
    if choice ==1:
        newTask = Task("FMA Update")
        with open("taskStorage.txt","w") as f:
            pickle.dump(newTask,f)
        print("Created task")


def main():
    #main function
    print("Code Started")
    while True:
        #Main loop

        #Main menu
        choice = menu()
        if choice == 3:
            #Write code here for saving the existing objects
            print("Closing the code")
            exit()
        elif choice == 1:
            startNewTask()

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
    main()
