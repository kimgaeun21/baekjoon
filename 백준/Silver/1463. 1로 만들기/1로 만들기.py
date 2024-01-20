INF = 987654321
n = int(input())

dp = [0]*(n+1)
for i in range(2, n+1):
    cnt1=INF
    cnt2=INF
    cnt3=INF
    if (i % 3) == 0:
        cnt3 = dp[i//3] + 1

    if (i % 2) == 0:
        cnt2 = dp[i//2] + 1

    cnt1 = dp[i-1] + 1

    dp[i] = min(cnt1, cnt2, cnt3)

print (dp[n])
    