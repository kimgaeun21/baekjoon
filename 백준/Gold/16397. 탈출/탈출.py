from  collections import deque

n , t, g = map(int, input().split())

answer = -1
visited=[0 for _ in range(100000)]

queue  = deque()
queue.append([n,0])
visited[n] = 1

while queue:
    x = queue.popleft()
    # print(x)
    v = x[0]
    n = x[1]
    if n > t:
        break
    if v == g:
        if n <= t:
            answer = n
            break
        else :
            answer = -1
            break

    if v + 1 < 100000 and visited[v+1] != 1:
        queue.append([v+1, n+1])
        visited[v+1] = 1
        
    if 0 <= v*2 < 100000:
        arr = list(map(int, str(v*2)))
        arr[0] -= 1
        next =''
        for i in arr:
            next += str(i)
        if visited[int(next)] != 1 and int(next) > 0:
            queue.append([int(next), n+1])
            visited[int(next)] = 1
             
if answer == -1:
    print('ANG')
else:
    print(answer)