n= int(input())
arr = []
for i in range(n):
    x = list(map(int, input().split()))
    arr.append(x)

dp = []
for i in range(n):
    if i == 0:
        dp.append(arr[0])
    else:
        x =[]
        for j in range(len(arr[i])):
            if j == 0:
                x.append(arr[i][0] + dp[i-1][0])
            elif j == len(arr[i])-1:
                x.append(arr[i][j] + dp[i-1][j-1])
            else:
                x.append(max(arr[i][j] + dp[i-1][j-1], arr[i][j] + dp[i-1][j]))
        dp.append(x)

print(max(dp[n-1]))