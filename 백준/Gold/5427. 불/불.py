from collections import deque

def bfs():
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    cnt = 0 
    
    while queue:
        cnt += 1
        while fire and fire[0][2] < cnt :
            x, y, time = fire.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < h and 0 <= ny < w:
                    if graph[nx][ny] == "." or graph[nx][ny] == "@":
                        graph[nx][ny] = "*"
                        fire.append((nx, ny, time + 1))

        while queue and queue[0][2] < cnt:
            x, y, time = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < h and 0 <= ny < w:
                    if graph[nx][ny] == "." and not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append((nx, ny, time + 1))
                else:
                    print(cnt)
                    return
                
    print("IMPOSSIBLE")
        


n = int(input())
for i in range(n):
    w, h = map(int, input().split())
    
    queue = deque()
    fire= deque()
    
    graph = []
    visited = [[0] * w for _ in range(h)]
    for i in range(h):
            graph.append(list(input().strip()))
            for j in range(w):
                if graph[i][j] == "@":
                    visited[i][j] = True
                    queue.append((i, j, 0))
                elif graph[i][j] == "*":
                    fire.append((i, j, 0))
    bfs()