from classes.TaskHandler import TaskHandler
import os
import time



def main():
    #main function
    print("Code Started")
    handler = TaskHandler()
    while True:
        #Main loop

        #Main menu
        choice = menu(handler)
        if choice == 3:
            #Write code here for saving the existing objects
            print("Closing the code")
            handler.dumpAll()
            exit()
        elif choice == 1:
            handler.startNewTask()
        
        elif choice == 2:
            handler.viewTasks()

        elif choice == 3:
            handler.selectTask()
            
        elif choice == 4:
            print("Closing code")
            handler.dumpAll()
            time.sleep(3)
            exit()

def menu(handler):
    print("----------------")
    print("1: Start new task")
    print("2: View tasks")
    print("3: Select a task")
    print("3: Exit the code")
    print("----------------")

    return handler.getChoice(4)
        

if __name__ == "__main__":
    os.chdir(r"C:\Users\millso\OneDrive - TPT Retirement Solutions\Desktop\CodeQuick\Dev\workFlow")
    main()
