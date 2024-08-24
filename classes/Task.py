from classes.Step import Step

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
        for rel in self.steps[self.spos].nextStepsRel:
            self.nextSteps.append(self.steps[self.spos+rel])
    
    def changeStep(self,spos):
        self.spos = spos
        self.getNextSteps()
        
    
    def getCurrentStep(self):
        return self.steps[self.spos].stepName


    def loadTaskSteps(self,taskType):
        return [Step("Update FMA Schedule",[1]),
                Step("Create ammendment letter",[1]),
                Step("Review FMA",[-2,1]),
                Step("Review Ammendment Letter",[-2,1]),
                Step("Send FMA documents to Leeds",[1]),
                Step("Save documents")
                ]