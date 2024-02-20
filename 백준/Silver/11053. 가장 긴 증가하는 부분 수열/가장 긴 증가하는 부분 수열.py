n = int(input())
arr = list(map(int, input().split()))
dp = [0 for i in range(max(arr)+1)]

for i in arr:
    dp[i] = max(dp[:i]) + 1

print(max(dp))