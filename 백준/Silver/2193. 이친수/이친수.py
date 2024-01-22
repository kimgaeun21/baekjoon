n = int(input())
arr = [0 for _ in range(n+1)]

if n == 1 or n == 2:
    print(1)
else:
    arr[1] = 1
    arr[2] = 1
    for i in range(3,n+1):
        arr[i] = arr[i-1] + arr[i-2]
    print(arr[n])