from itertools import combinations

n, x= map(int, input().split())

array= list(input().split())
array.sort()
combi=[]

for i in combinations(array,n):
    combi.append(i)

for i in range(len(combi)):
    x = 0
    if 'a' in combi[i]:
        x = x + 1
    if 'e' in combi[i]:
        x = x + 1
    if 'i' in combi[i]:
        x = x + 1
    if 'o' in combi[i]:
        x = x + 1
    if 'u' in combi[i]:
        x = x + 1
    
    if x < 1:
        continue
    elif n-x < 2:
        continue
    
    for j in range(n-1):
        print(combi[i][j], end='')
    print(combi[i][n-1])

