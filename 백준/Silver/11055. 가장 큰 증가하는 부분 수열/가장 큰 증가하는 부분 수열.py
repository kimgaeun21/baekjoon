n = int(input())
arr = list(map(int,input().split()))
dp = [0 for _ in range(1001)]

for i in range(n):
    x = arr[i]
    dp[x] = x + max(dp[:x])

print(max(dp))