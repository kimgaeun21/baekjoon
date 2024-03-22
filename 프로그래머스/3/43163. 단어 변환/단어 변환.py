from collections import deque

def bfs(graph, start, target):
    answer = 0
    queue = deque()
    queue.append([start,0])
    graph[start][0] = True
    
    while queue:
        x,t = queue.popleft()
        if x == target:
            return t
        for i in graph[x][1:]:
            if not graph[i][0]:
                queue.append([i,t+1])
                graph[i][0] = True
    return 0
    
def solution(begin, target, words):
    answer = 0
    graph = {begin:[False]}

    for i in words:
        graph[i] = [False]
    
    for i in graph.keys():
        for j in words:
            x = 0
            for k in range(len(j)):
                if i[k] != j[k]:
                    x += 1
            if x < 2:
                graph[i].append(j)
    
    return bfs(graph, begin, target)
    
    