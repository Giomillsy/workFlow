import pickle
import os

class TaskHandler:
    def __init__(self):
        
        self.storagefn = 'taskStorage.pkl' # Filename of storage

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