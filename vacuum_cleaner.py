import random
class theWorldOfCleaner():
    def __init__(self):
        self.status = {'loc_A' : random.choice(['Clean','Dirty']),'loc_B' : random.choice(['Clean','Dirty'])}
        self.done = False
    def move_it(self,agent,move):
        if(move == 'Right'):
            agent.location = 'loc_B'
            agent.performance -= 1
        elif(move == 'Left'):
            agent.location = 'loc_A'
            agent.performance -= 1
        elif(move == 'Vacuum'):
            
            if(self.status[agent.location] == 'Dirty'):
                
                agent.performance += 10
                self.status[agent.location] == 'Clean'
        if(self.status['loc_A'] == 'Clean' and self.status['loc_B'] == 'Clean'):
            self.done = True
    def random_start(self):
        return random.choice(['loc_A','loc_B'])
class Agent():
    def __init__(self,location):
        self.performance = 0
        self.location = location
    def move_sec(self):
        return random.choice(['Right','Left','Vacuum'])
    
env = theWorldOfCleaner()
agent = Agent(env.random_start)

while(not env.done):
    agent_move = agent.move_sec()
    print (agent_move)
    env.move_it(agent,agent_move)
    print (agent.location)
    print (env.status)
    
print(agent.performance)
