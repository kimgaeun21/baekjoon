from collections import deque

n, m, t = map(int,input().split())
TIME = t
graph=[]
gram =[0, 0, t]
gram_graph=[[0 for _ in range(m)] for _ in range(n)]


for _ in range(n):
    x = list(map(int, input().split()))
    graph.append(x)
    
def dfs(x,y,t,graph):
    
    queue = deque()
    queue.append((x, y, t))
    graph[x][y] = 1
    
    dx=[-1, 1, 0, 0]
    dy=[0, 0, -1, 1]
    
    while queue:
        tmp = queue.popleft()
        t = tmp[2]
        
        if tmp[0] == n-1 and tmp[1] == m-1:
            return t
        
        for i in range(4):
            nx = tmp[0] + dx[i]
            ny = tmp[1] + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            
            if graph[nx][ny] == 0:
                queue.append((nx, ny, t+1))
                graph[nx][ny] = 1
            
            if graph[nx][ny] == 2:
                global gram
                
                if t+1 < gram[2]:
                    gram =[nx,ny, t+1]
                
    return TIME + 1

find = dfs(0,0,0,graph)

gram_find = dfs(gram[0], gram[1], gram[2],gram_graph)

if min(find,gram_find) <= t:
    print(min(find,gram_find))
else:
    print("Fail")

