from collections import deque
def bfs(graph, start, visited, end):
    queue = deque([[start,0]])
    visited[start] = 1
    
    while queue:
        x = queue.popleft()
        v = x[0]
        n = x[1]
        if v == end:
            return n
    
        for i in graph[v]:
            
            if visited[i] != 1:
                queue.append([i,n+1])
                visited[i] = 1
    
            

n, k = map(int,input().split())
graph =[]

for i in range(200003):
    graph.append([])
    
graph[0].append(1)
maxi= max(n,k)   

for i in range(1,maxi+2):
    if i-1 not in graph[i]:
        graph[i].append(i-1)
    
    if i+1 not in graph[i]:
        graph[i].append(i+1)
    
    if 2*i not in graph[i] :
        graph[i].append(2*i)
        
visited=[0] * (200003)
print(bfs(graph,n,visited, k))
        
