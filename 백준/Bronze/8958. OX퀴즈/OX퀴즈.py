n= int(input())

for i in range(n):
    x = list(str(input()))
    dp = [0 for _ in range(len(x))]
    if x[0] =='O':
        dp[0] = 1
    for j in range(1,len(x)):
        if x[j] == 'O':
            dp[j] = dp[j-1] +1
    print(sum(dp))
    