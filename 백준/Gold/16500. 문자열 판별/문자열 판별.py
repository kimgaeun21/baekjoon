s = input()
n = int(input())

arr = [input() for _ in range(n)]
dp = [0 for _ in range(len(s) + 1)]
dp[0] = 1


for i in range(len(s)):
    if dp[i] == 0:
        continue
    for j in range(n):
        if s.find(arr[j], i) == i:
            dp[i + len(arr[j])] = 1

print(dp[len(s)])