class Environment: 
    def __init__(self,name,distance,rating):
        self.name=name
        self.distance=distance
        self.rating=rating
        self.utility=0
    
    def calculate_utility(self):
        self.utility=self.rating-self.distance
        return self.utility

class UtilityAgent:
    def __init__ (self, restaurants):
        self.restaurants=restaurants
    
    def select(self):
        for restaurant in self.restaurants:
            restaurant.calculate_utility()
            print(f"Restaurant : {restaurant.name}, Utility : {restaurant.utility}")
        selected = self.restaurants[0]
        for restaurant in self.restaurants:
            if restaurant.utility > selected.utility:
                selected=restaurant
        
        print(f"\nSelected Restaurant : {selected.name}")
        

rA=Environment("A",3,7)
rB=Environment("B",5,9)

agent=UtilityAgent([rA,rB])
agent.select()
            
