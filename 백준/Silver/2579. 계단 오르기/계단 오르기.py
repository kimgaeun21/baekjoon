def dp(arr,n):
    dp = [[] for _ in range(n)]
    dp[0].append((arr[0], 1))
    dp[1].append((arr[1]+arr[0], 2))
    dp[2].append((arr[0]+arr[2], 1))
    dp[2].append((arr[1]+arr[2], 2))

    for i in range(3,n):
        maxi = (0,0)
        for j in dp[i-2]:
            if maxi[0] < j[0]+arr[i]:
                maxi=(j[0]+arr[i], 1)
        dp[i].append(maxi)
                
        maxi = (0,0)
        for j in dp[i-1]:
            if j[1]+1 !=3:
                if maxi[0] < j[0]+arr[i]:
                    maxi=(j[0]+arr[i], j[1]+1)
        dp[i].append(maxi)
                    
    print(max(dp[n-1], key = lambda x : x[0])[0])
            
n = int(input())
arr = [int(input()) for _ in range(n)]

if n == 1:
    print(arr[0])
elif n==2:
    print(arr[1]+arr[0])
else:
    dp(arr,n)


    

    