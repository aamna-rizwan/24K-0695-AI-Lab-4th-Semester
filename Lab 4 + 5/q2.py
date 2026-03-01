graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': [],
    'F': ['H'],
    'G': [],
    'H': []
}

def dls(node,goal,limit,path=None,visited=None):
    if path is None:
        path=[]
    if visited is None:
        visited=[]
    visited.append(node)
    path.append(node)
    if node==goal:
        return True, visited, path
    if limit<=0:
        path.pop()
        return False,visited ,path
    for neighbour in graph.get(node,[]):
         found,visited,result=dls(neighbour,goal,limit-1,path,visited)
         if found:
             return True,visited,result
    
            
    path.pop()
    return False,visited,path
    
start='A'
goal='H'

print("dls with depth limit 2")
found,visited2,path2=dls(start,goal,2)
print("Visited nodes : ", visited2)
if found:
    print("path : ",path2)
else:
    print("goal not found in depth limit")

print("\ndls with depth limit 3")
found,visited3,path3=dls(start,goal,3)
print("Visited nodes : ", visited3)
if found: 
    print("Path : " ,path3 )
else:
    print("goal not found in depth limit")

            
