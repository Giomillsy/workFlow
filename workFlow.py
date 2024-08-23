from classes.TaskHandler import TaskHandler
import os



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
            handler.startNewTask()
        
        elif choice == 2:
            handler.viewTasks()

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
