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

def dls_ids(node,goal,limit,path=None):
    if path is None:
        path=[]
    path.append(node)
    if node==goal or limit==0:
        return node ==goal,path
    if limit<=0:
        path.pop()
        return False,path
    for neighbour in graph.get(node,[]):
        found,result=dls_ids(neighbour,goal,limit-1,path)
        if found:
             return True,result
        else:
            return False,path
    
            
    path.pop()
    return False,path


def ids(start,goal,max_depth=10):
    for depth in range(max_depth+1):
        print("\n searching with dl = " , depth)
        found,path=dls_ids(start,goal,depth)
        print("Nodes visited : ",path)
        if found: 
            print("\nGoal found!")
            print("Path : ",path)
            return path
        else:
             print("Goal not found at this dl")
        
    return None
        
start='A'
goal='G'       
final_path=ids(start,goal)
