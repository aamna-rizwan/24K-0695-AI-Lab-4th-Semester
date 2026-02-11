class Environment:
    def __init__ (self):
        self.rooms={ 'a' : " ", 'b' : " " , 'c' : "F" , 'd' : " ", 'e' : "F" , 'f' : " ", 'g' : " ", 'h' : " ", 'j' : "F"}
    
    def display(self):
        print("\nCurrent Environment Status : ")
        print(self.rooms['a'], "|", self.rooms['b'], "|", self.rooms['c'])
        print(self.rooms['d'], "|", self.rooms['e'], "|", self.rooms['f'])
        print(self.rooms['g'], "|", self.rooms['h'], "|", self.rooms['j'])

class Robot: 
    def __init__ (self,path):
        self.path=path
    
    def act(self,environment):
        for room in self.path:
            print("\nRobot moved to room : ",room)
            if environment.rooms[room]=='F':
                print("Extinguishing fire in room :" , room)
                environment.rooms[room]= " "
            else:
             print(f"Room {room} is safe")
            
            environment.display()
            
path=['a','b','c','d','e','f','g','h','j']
environment=Environment()
robot=Robot(path)
robot.act(environment)
environment.display()
            
