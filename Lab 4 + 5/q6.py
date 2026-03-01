graph = {
    'A': {'B': 4, 'C': 3},
    'B': {'E': 12, 'F': 5},
    'C': {'D': 7, 'E': 10},
    'D': {'E': 2},
    'E': {'G': 5},
    'F': {'G': 16},
    'G': {}
}

heuristic = {
    'A': 14, 'B': 12, 'C': 11,
    'D': 6,  'E': 4,  'F': 11,
    'G': 0
}

start='A'
goal='G'

import heapq
import random

def reconstruct(goal,came_from):
    path=[]
    node=goal
    while node is not None:
        path.append(node)
        node=came_from[node]
    path.reverse()
    return path
    
def aStar(start,goal):
    frontier=[]
    heapq.heappush(frontier, (heuristic[start],start))
    g_costs={}
    g_costs[start]=0
    came_from={}
    came_from[start]=None
    
    while frontier:
        current_f,current_node=heapq.heappop(frontier)
        
        if current_node==goal:
            path=reconstruct(goal,came_from)
            print("Optimal Path : ",path)
            print("Total Cost : ", g_costs[goal])
            return path
        
        if current_node in graph and graph[current_node]:
            neighbours=graph[current_node]
            for neighbour in neighbours: 
                cost =neighbours[neighbour]
                new_g=g_costs[current_node]+cost
                f_cost=new_g +heuristic[neighbour]
                
                if neighbour not in g_costs or new_g<g_costs[neighbour]:
                    g_costs[neighbour]=new_g
                    came_from[neighbour]=current_node
                    heapq.heappush(frontier,(f_cost,neighbour))
    
    print("Goal not reachable")
    return None

def update_random_edge():
    nodes_with_edges = []
    for n in graph:
        if graph[n]:
            nodes_with_edges.append(n)
    u = random.choice(nodes_with_edges)
    v = random.choice(list(graph[u].keys()))
    old_cost = graph[u][v]
    change = random.randint(-3, 5)
    new_cost = old_cost + change
    if new_cost < 1:
        new_cost = 1
    graph[u][v] = new_cost
    print(f"Edge changed: {u}->{v} | {old_cost}->{new_cost}")


print("Initial Search:")
aStar(start,goal)

for i in range(2):
    update_random_edge()
    print("\nRecomputing after change:")
    aStar(start,goal)



    
