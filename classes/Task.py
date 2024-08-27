from classes.Step import Step
import os
class Task:
    def __init__(self,taskType):
        self.taskType = taskType
        self.steps = self.loadTaskSteps(self.taskType)
        self.spos = 0
        self.getNextSteps()
        self.description = input("Please write a short description to dsiplay for furture users:")

    def getNextSteps(self):
        #Gets the next possible steps in the work flow
    
        self.nextSteps = []
        for rel in self.steps[self.spos].relSpos:
            self.nextSteps.append(self.spos+rel)
    
    def changeStep(self,spos):
        self.spos = spos
        self.getNextSteps()

    def showProcedure(self):
        os.startfile(self.steps[self.spos].procedureLoc)
        print("Opened file")
    
    def getCurrentStep(self):
        return self.steps[self.spos].stepName


    def loadTaskSteps(self,taskType):
        #Load the taskType
        if taskType == "FMA Update":
            return [Step("Update FMA Schedule",[1]),
                    Step("Create ammendment letter",[1]),
                    Step("Review FMA",[-2,1]),
                    Step("Review Ammendment Letter",[-2,1]),
                    Step("Send FMA documents to Leeds",[1]),
                    Step("Save documents")]
        
        elif taskType == "GEF":
            return [
                Step("GEF at PreOk on blotter",[1],procedureLoc=r"\\srv12r2fs01\inv\0. Investment Documentation\Procedures\1.5 Portfolio Modelling\GEF Rebalance.docx"),
                Step("Review the GEF",procedureLoc=r"\\srv12r2fs01\inv\0. Investment Documentation\Procedures\1.5 Portfolio Modelling\GEF Rebalance.docx")
            ]
        
        else:
            print("Dev Error: NO taskType found in loadTaskSteps")