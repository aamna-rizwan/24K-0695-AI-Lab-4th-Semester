class Environment: 
    def __init__ (self,traffic='Heavy'):
        self.traffic=traffic
    def get_percept(self):
        return 'Heavy' if self.traffic=='Heavy' else 'Light'

class SimpleReflexAgent:
    def __init__ (self):
        pass
    def act(self,percept):
        if percept=="Heavy":
            return "Green for longer"
        else:
            return "Normal green"
            

def run_agent(agent,environment):
    percept=environment.get_percept()
    action=agent.act(percept)
    print(f"Percept : {percept}, Action : {action}")

agent=SimpleReflexAgent()
environment=Environment("Heavy")

run_agent(agent,environment)
