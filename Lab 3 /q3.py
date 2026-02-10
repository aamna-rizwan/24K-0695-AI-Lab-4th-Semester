class Environment: 
    def __init__ (self):
        self.subjects=["AI","Math","Physics"]
    
class GoalAgent:
    def __init__ (self,goal):
        self.goal=goal
        self.completed=[]
    def act(self,environment):
        for subject in environment.subjects:
            if subject not in self.completed:
                print("Studying : ",subject)
                self.completed.append(subject)
    def goalDone(self):
        if(len(self.completed)==3):
            return True
        else: 
            return False

environment=Environment()
agent=GoalAgent("Complete all subjects")

agent.act(environment)
if agent.goalDone(): 
    print("Goal acheived : all subejects completed")
