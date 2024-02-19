cnt = 0
def dfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    if x< 0 or x>=n or y < 0 or y>=n:
        return False
    
    if graph[x][y]==1:
        graph[x][y] = 0
        global cnt 
        cnt += 1
        for i in range(4):
            dfs(x+dx[i], y+dy[i])
        return True
    return False

n = int(input())
graph=[]

for i in range(n):
    graph.append([])
    x= input()
    for j in range(len(x)):
        graph[i].append(int(x[j]))
        

cnt_array=[]
for i in range(n):
    for j in range(n):
        if dfs(i,j) ==True:
            cnt_array.append(cnt)
            cnt = 0
        
print(len(cnt_array))
cnt_array.sort()
for i in cnt_array:
    print(i)