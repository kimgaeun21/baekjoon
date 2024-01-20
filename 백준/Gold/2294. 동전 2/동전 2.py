n, k = map(int, input().split())
arr = [98765 for _ in range(k+1)]
coins=[]
for i in range(n):
    x = int(input())
    if x <= k:
        coins.append(x)
        arr[x] = 1
    
for i in range(k+1):
    for j in coins:
        arr[i] = min(arr[i], arr[i-j]+1)

if arr[k] == 98765:
    print(-1)
else: 
    print(arr[k])