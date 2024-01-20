def solution(n, arr1, arr2):
    answer = 0
    dp1=[0 for _ in range (n)]
    dp2=[0 for _ in range (n)]
    
    dp1[0] = arr1[0]
    dp2[0] = arr2[0]
    
    if n == 1:
        return max(dp1[0], dp2[0])
    
    dp1[1] = arr1[1] + dp2[0]
    dp2[1] = arr2[1] + dp1[0]
    
    if n ==2:
        return max(dp1[1], dp2[1])
    
    for i in range(2,n):
        dp1[i] = arr1[i] + max(dp1[i-2], dp2[i-1], dp2[i-2])
        dp2[i] = arr2[i] + max(dp2[i-2], dp1[i-1], dp1[i-2])
    
    answer = max(max(dp1), max(dp2))
    return answer

t = int(input())
for i in range (t):
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int,input().split()))
    print(solution(n, arr1, arr2))