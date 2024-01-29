from collections import deque

def solution(a, b):
    visited = [0 for _ in range(10000)]
    
    queue = deque()
    queue.append([a, ''])
    visited[a] = 1
    
    while queue:
        v, n = queue.popleft()

        if (v == b):
            return n
        
        if visited[v*2%10000] != 1:
            queue.append([v*2%10000, n+'D'])
            visited[v*2%10000] = 1
        
        if visited[(v-1)%10000] != 1:
            queue.append([(v-1)%10000, n+'S'])
            visited[(v-1)%10000] = 1
            
        n_l =  v // 1000 + (v % 1000)*10
        n_r = v // 10 + (v % 10) * 1000
        
        if visited[n_l] != 1:
            queue.append([n_l, n+'L'])
            visited[n_l] = 1
           
        if visited[n_r] != 1:
            queue.append([n_r, n+'R'])
            visited[n_r] = 1
    
            
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    answer = solution(a, b)
    print(answer)
