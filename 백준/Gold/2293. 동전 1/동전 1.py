n, k = map(int, input().split())
coin=[0 for i in range(n)]
for i in range(n):
    coin[i] = int(input())
    
dp=[0 for i in range(k+1)]
coin.sort()

for i in coin:
    for j in range(i,k+1):
        if j == i :
            dp[j] = dp[j] + 1
        else:
            dp[j] = dp[j] +dp[j-i]
    
print(dp[k])
