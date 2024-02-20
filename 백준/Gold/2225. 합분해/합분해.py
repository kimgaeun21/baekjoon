n, k = map(int, input().split())

dp = [[0 for _ in range(n+1)] for _ in range(k)]
dp[0] = [1 for _ in range(n+1)]
for i in range(1,k):
    for j in range(n+1):
        dp[i][j] = (sum(dp[i-1][:j])+dp[i-1][j])%1000000000


print(dp[k-1][n])

