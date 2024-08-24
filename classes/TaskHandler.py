import pickle
import os
from classes.Task import Task

class TaskHandler():
    def __init__(self):
        
        self.storagefn = 'taskStorage.pkl' # Filename of storage
        self.taskTypes ={
            1:"FMA Update",
            2:"GEF"
        }
        self.tasks = []
        f = self.openStorageFile(self.storagefn,"rb")
        with f:
            while True:
                try:
                    self.tasks.append(pickle.load(f))
                except:
                    #No more objects in file
                    break


    def dumpAll(self):
        #Saves all objects in pickle file
        f = self.openStorageFile(self.storagefn,"wb")
        with f:
            #Deletes all contents in file
            pass
        
        f = self.openStorageFile(self.storagefn,"wb")
        with f:
            for task in self.tasks:
                pickle.dump(task,f)
    
    def openStorageFile(self,fn,openType):
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
    
    def viewTasks(self):
    
        for i in range(len(self.tasks)):
            print(f'{i+1}: {self.tasks[i].taskType} - {self.tasks[i].description}')

    def selectTask(self):
        print("-----------")
        print("Select one of the below")
        self.viewTasks()
        print("-------------")
        choice = self.getChoice(len(self.tasks))
        task = self.workOnTask(self.tasks[choice-1])

        if task == "Complete":
            del self.tasks[choice-1]

        else:
            self.tasks[choice-1] = task

    def workOnTask(self,task):
        #Allow the user to work on a task until they're finished
        while True:
            print(f"The current step is {task.getCurrentStep()}")
            print("---------------")
            print("Select an option")
            print("1: Mark current step as finished")
            print("2: Open procedure for current step")
            print("3: Exit to main menu")
            print("----------------")
            choice = self.getChoice(3)
            if choice == 1:
                spos = self.selectNextStep(task)
                if spos is not None:
                    task.changeStep(spos)      
                    if task.nextSteps == []:
                        print("Task complete!")
                        return "Complete"
            elif choice == 2:
                task.showProcedure()
            elif choice ==3:
                return task
        
    def selectNextStep(self,task):
        print("Select the next step from below")
        for i in range(len(task.nextSteps)):
            print(f"{i+1}: {task.steps[task.nextSteps[i]].stepName}")
        print(f"{i+2}: Cancel finishing the step")
        print("----------------")
        choice = self.getChoice(i+2)
        if choice == i+2:
            return None
        else:
            return (task.nextSteps[choice-1])

    def startNewTask(self):
        print("-----------")
        print("Select one of the below to create it as a task")
        for i in range(len(self.taskTypes)):
            print(f"{i+1}: {self.taskTypes[i+1]}")
        print(f"{i+2}: Exit back to main menu")
        print("--------------")

        choice = self.getChoice(i+2)
        if choice != i+2:
            newTask = Task(self.taskTypes[i+1])
            self.tasks.append(newTask)
    
    def getChoice(self,maxChoice):
        #Error catching
        try:
            choice = int(input("Please enter an option:"))
        except ValueError:
            print("You did not enter a number. Can you try again please")

        if choice not in range(1,maxChoice+1):
            print("You did not enter a valid number. Can you try again please")

        return choice      