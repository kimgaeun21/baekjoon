n= int(input())
dp = list(map(int, input().split()))
dp.insert(0, 0)

if n ==1:
    print(dp[1])
else:
    for i in range(1,n+1):
        for j in range(i//2, i+1):
            dp[i] = max(dp[i], dp[i-j]+dp[j])

print(dp[n])