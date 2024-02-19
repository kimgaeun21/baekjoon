n = int(input())
dp = [[0 for _ in range(10)] for _ in range(n)]
dp[0] = [1,1,1,1,1,1,1,1,1,1]

if n==1:
    print(sum(dp[0]))
else:
    for i in range(1,n):
        for j in range(10):
            dp[i][j] = sum(dp[i-1][:j+1])%10007
    
    print(sum(dp[n-1])%10007)