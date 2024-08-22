class Task:
    def __init__(self):
        self.taskType = "FMA Update"
        self.steps = loadTaskSteps(self.taskType)

class Step:
    def __init__(self,stepName,nextSteps = [], end=False):
        self.stepName = stepName
        self.nextSteps = nextSteps
        self.end = end


def loadTaskSteps(taskType):
    return [Step("Update FMA Schedule",[1]),
            Step("Create ammendment letter",[1]),
            Step("Review FMA",[-2,1]),
            Step("Review Ammendment Letter",[-2,1]),
            Step("Send FMA documents to Leeds",[1]),
            Step("Save documents",end=True)
            ]

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
        

def menu():
    print("----------------")
    print("1: Start new task")
    print("2: View tasks")
    print("3: Exit the code")
    print("----------------")

    
    #Error catching
    try:
        choice = int(input("Please enter an option:"))
    except ValueError:
        print("You did not enter a number. Can you try again please")

    if choice < 1 or choice >3:
        print("You did not enter a valid number. Can you try again please")

    return choice
        

if __name__ == "__main__":
    main()
