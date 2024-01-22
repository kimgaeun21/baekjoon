import math
n = int(input())
arr = [i**2 for i in range(int(math.sqrt(n))+1)]
arr.sort(reverse=True)
dp = [987654321 for i in range(n+1)]

for i in arr:
    dp[i] = 1
    
for i in range(2, n+1):
    for j in arr:
        if i >= j:
            dp[i] = min(dp[i],dp[i-j] + dp[j])
            
print(dp[n])