import random 

class Environment: 
    def __init__(self):
        self.state="Start"
        self.rewards={"Play":5, "Rest":1}
    def get_percept(self):
        return self.state
    def action(self,action):
        reward=self.rewards[action]
        return reward

class LearningAgent:
    def __init__(self,actions):
        self.Q={}
        self.actions=actions
        self.alpha=0.1
        self.gamma=0.9
        self.epsilon=0.1
        
    def get_Q_value(self,state,action):
        return self.Q.get((state,action),0.0)
        
    def select_action(self,state):
        if random.uniform(0,1) < self.epsilon:
            return random.choice(self.actions)
        else:
            return max(self.actions,key=lambda a:self.get_Q_value(state,a))
    
    def learn(self, state, action, reward, next_state):
        old_Q = self.get_Q_value(state,action)
        best_future_Q=max([self.get_Q_value(next_state,a) for a in self.actions])
        self.Q[(state,action)] = old_Q + self.alpha*(reward +self.gamma*best_future_Q - old_Q)
    
    def act(self,state): 
        action =self.select_action(state)
        return action

def run_agent(agent,environment,steps):
    for step in range(steps):
        state=environment.get_percept()
        action=agent.act(state)
        reward= environment.action(action)
        print(f"Step {step+1} , Action : {action}, Reward {reward}")
        next_state=environment.get_percept()
        agent.learn(state,action,reward,next_state)
        print("\nQ-table updated : " , agent.Q)

agent=LearningAgent(["Play","Rest"])
environment=Environment()

run_agent(agent,environment,10)
        
