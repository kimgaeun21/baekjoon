from collections import deque

def dfs(graph, start, visited):
    visited[start] = 1
    print(start, end =' ')

    for i in graph[start]:
        if visited[i] == 0:
            dfs(graph, i , visited)

def bfs(graph, start, visited):
    print("\n", end='')
    queue = deque([start])
    visited[start] = 1
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if visited[i]==0:
                queue.append (i)
                visited[i] = 1

n, m, v= map(int, input().split())
g=[]
for i in range(n+1):
    g.append([])



for i in range(m):
    x, y = map(int, input().split())
    if not (y in g[x]):
        g[x].append(y)
    if not(x in g[y]):
        g[y].append(x)

for i in range(n+1):
    g[i].sort()

visited_d = [0]*(n + 1)

dfs(g, v, visited_d)


visited_b = [0]*(n+1)

bfs(g, v, visited_b)