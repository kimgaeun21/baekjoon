from collections import deque

def bfs(x, y, z):
    queue = deque()
    queue.append((x,y,z))
    graph[x][y][z] = 1

    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]
    
    while queue:
        x, y, z = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            
            if nx < 0 or ny < 0 or nz< 0 or nx >= l or ny>=r or nz >= c:
                continue
            
            if graph[nx][ny][nz] =='E':
                print("Escaped in {0} minute(s).".format(graph[x][y][z]))
                return  
            
            if graph[x][y][z] =='#':
                continue
            
            if graph[nx][ny][nz] == '.':
                graph[nx][ny][nz] = graph[x][y][z] + 1
                queue.append((nx, ny, nz))

    print('Trapped!')
                
        
while True:
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0:
        break
    
    graph = [[[]*c for _ in range(r)] for _ in range(l)]
    start =(0, 0, 0)
    for i in range(l):
        graph[i] = [list(map(str, input().strip())) for _ in range(r)]
        input()
    
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if graph[i][j][k] =='S':
                    bfs(i, j, k)
  