from itertools import combinations

n, s = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0

for i in range(1,n+1):
    a = combinations(arr,i)
    for j in a:
        if sum(j) == s:
            answer += 1
            
print(answer)