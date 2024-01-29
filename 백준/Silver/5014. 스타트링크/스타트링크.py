from collections import deque
def bfs(graph, start, visited, end):
    queue = deque()
    queue.append([start, 0])
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
    return "use the stairs"
        
        
f, s, g, u, d = map(int, input().split())

graph = [[]for i in range(f+1)]


for i in range(1, f+1):
    if i - d > 0:
        graph[i].append(i - d)
    
    if i + u < f+1:
        graph[i].append(i+u)
        
visited =[0 for i in range(f+1)]
answer = bfs(graph, s, visited, g)
print(answer)
        
