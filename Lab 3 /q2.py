import random

class Environment: 
    def __init__(self):
        self.present=random.choice(["yes","no"])
        self.light= "off"
    def get_percept(self):
        self.present=random.choice(["yes","no"])
        return self.present,self.light

class ModelAgent: 
    def __init__ (self):
        self.modelPresent=None
        self.modelLight=None
    
    def act(self,percept):
        students, light1=percept
        
        if students=="yes" and light1=="off":
            action="Turn lights ON"
            lightStatus="on"
        elif students=="no" and light1=="on":
            action="Turn lights OFF"
            light="off"
        else:
            action = "do nothing"
        
        self.modelPresent=students
        self.modelLight=light1
        
        return action,light1
    
    def display(self):
        print(f" Prev students present : {self.modelPresent}")
        print(f"Prev Light Status : {self.modelLight}")

environment=Environment()
agent=ModelAgent()

for i in range(1,9):
    print("\nStep : ",i)
    percept=environment.get_percept()
    action,new_light=agent.act(percept)
    environment.light=new_light
    print(f"Percept for Students : {percept[0]}, Lights : {percept[1]}, Action = {action}")
    agent.display()
    
