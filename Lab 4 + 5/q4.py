graph={
    'S':{'A':4,'B':2},
    'A':{'C':5, 'D':10},
    'B':{'E':3},
    'C':{'G':4},
    'D':{'G':1},
    'E':{'D':4},
    'G':{}
}
start='A'
goal='G'

import heapq

def ucs(graph,start,goal):
    frontier=[(0,start,[start])] #cost, node,path
    explored=set()
    while frontier:
        cost,node,path=heapq.heappop(frontier)
        if node==goal:
            return path,cost
        if node not in explored:
            explored.add(node)
            for neighbour,edge in graph.get(node,{}).items():
                if neighbour not in explored:
                    heapq.heappush(frontier,(cost+edge,neighbour,path + [neighbour]))
    
    return None
    
path,total_cost=ucs(graph,start,goal)
print("Least cost path : ",path)
print("Total cost: ",total_cost)
