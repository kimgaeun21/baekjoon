n = int(input())
arr =[]
for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = []
dp.append(arr[0])

for i in range(1,n):
    rgb =[0, 0, 0]
    rgb[0] = min(dp[i-1][1]+arr[i][0], dp[i-1][2]+arr[i][0])
    rgb[1] = min(dp[i-1][0]+arr[i][1], dp[i-1][2]+arr[i][1])
    rgb[2] = min(dp[i-1][0]+arr[i][2], dp[i-1][1]+arr[i][2])
    dp.append(rgb)
    
print(min(dp[n-1]))
    