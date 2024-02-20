t = int(input())
n=[]
for i in range(t):
    n.append(int(input()))
    
dp = [0 for _ in range(max(n))]

if max(n) > 3:
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1
    for i in range(3,len(dp)):
        dp[i] = dp[i-3]+dp[i-2]
else:
    for i in range(len(dp)):
        dp[i] = 1
    
for i in n:
    print(dp[i-1])