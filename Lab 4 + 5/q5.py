graph = {
        'S': [('A', 3), ('B', 6), ('C',5)],
        'A': [('D', 9), ('E', 8),('S',3)], 
        'B': [('F', 12), ('G', 14),('S',6)],
        'C': [('H', 7),('S',5)], 
        'D': [('A',9)],
        'E': [('A',8)], 
        'F': [('B', 12)],
        'G': [('B', 14)],
        'H': [('I', 5), ('J', 6),('C', 7)], 
        'I': [('K', 1), ('L', 10), ('M', 2),('H',5)], 
        'J': [('H',6)],
        'K': [('I',1)], 
        'L': [('I',10)],
        'M': [('I',2)]
}

#because the graph in q does not allow undirected edges i.e. you cannot go from S to A without losing the path. and because we have multiple goals so it shows no path found if the graph was directed, because it does not have any single path because multiple goals 
#to allow this we would need to add e.g. S={A:3} so A={S:3}
#i have hence added those edges for the algorithm to work correctly
start='S'
goals=['I', 'J']

import heapq

def best_first(graph,start,goals):
    frontier=[]
    heapq.heappush(frontier,(0,start,[start],set()))
    visited=set()
    while frontier:
        cost,node,path,goals_visited=heapq.heappop(frontier)
        
        if node in goals:
            goals_visited = goals_visited | {node} # union of vis goals and node
            
        state=(node, tuple(sorted(goals_visited)))
        if state in visited:
            continue
        visited.add(state)
       
        if goals_visited==set(goals):
                return path,cost
            
        for neighbour,edge in graph.get(node,[]):
            heapq.heappush(frontier, (cost+edge,neighbour,path+[neighbour],goals_visited))
   
    return None,None 

path,total_cost=best_first(graph,start,goals)
if path:
    print("Least cost path : ",path)
    print("Total cost: ",total_cost)
else: 
    print("no path found :(")

