from collections import deque

def bfs(graph, visited, start):
    queue = deque()
    if not visited[start]:
        queue.append(start)
        visited[start] = True
    else:
        return False
    
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return True
        
def solution(n, computers):
    answer = 0
    visited=[False]*n
    graph=[]
    for i in range(len(computers)):
        graph.append([])
        for j in range(len(computers[i])):
            if computers[i][j] == 1:
                graph[i].append(j)
                
    for i in range(n):
        if bfs(graph, visited, i)==True:
            answer += 1
            
    return answer