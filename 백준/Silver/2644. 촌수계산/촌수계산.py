from collections import deque

def bfs (graph, start, visited, end):
    queue= deque([[start,0]])
    visited[start]=1
    arr=[]
    while queue:
        x = queue.popleft()
        arr.append(x)
        v = x[0]
        n = x[1]
        if v == end:
            return n
        for i in graph[v]:
            if visited[i] == 0:
                queue.append([i,n+1])
                visited[i] = 1
    return -1
                
n = int(input())
start, end = map(int, input().split())
m = int(input())
graph=[]
for _ in range(n+1):
    graph.append([])

for _ in range(m):
    a, b = map(int, input().split())
    if b not in graph[a]:
        graph[a].append(b)
    
    if a not in graph[b]:
        graph[b].append(a)
    
for i in range(n):
    graph[i].sort()
    
visited=[0] * (n+1)
answer = bfs(graph,start,visited,end)
print(answer)