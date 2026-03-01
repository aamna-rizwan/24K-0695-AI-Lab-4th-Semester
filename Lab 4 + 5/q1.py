building = [
    [1, 1, 0, 1],
    [0, 1, 1, 1],
    [1, 1, 0, 1],
    [1, 0, 1, 1]
]

rows=len(building)
cols=len(building[0])
directions=[(-1,0),(1,0),(0,-1),(0,1)]

graph={}
for i in range(rows):
    for j in range(cols):
        if building[i][j]==1:
            neighbours=[]
            for x,y in directions: 
                ni=i+x
                nj=j+y
                if 0<=ni<rows and 0<=nj<cols and building[ni][nj]==1:
                    neighbours.append((ni,nj))
            graph[(i,j)]=neighbours
            
print("Adjacency List : ")
for node in graph: 
    print(f"{node}:{graph[node]}")

start1=(0,0)
end1=(3,3)   
    
def bfs(graph,start,goal):
    visited=set()
    queue=[(start,[start])]
    visited.add(start)
    while queue: 
        node,path=queue.pop(0)
        print(node, end="")
        if node==goal:
            print("\nGoal found\n")
            return path
        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour,path+[neighbour]))
    
    return None


print("")
path=bfs(graph,start1,end1)
print("shortest path")
print(path)
