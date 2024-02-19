import sys
input = sys.stdin.readline

n= int(input())
arr=[]
for _ in range(n):
    arr.append(tuple(map(int, input().split())))

arr.sort()

total = 0
start = arr[0][0]
end = arr[0][1]

for i in range(1,n):
    if arr[i][1]<=end:
        continue
    if arr[i][0] > end:
        total += end-start
        start = arr[i][0]
        end = arr[i][1] 
    elif arr[i][0] <= end:
        end = arr[i][1]
        
total += end- start
print(total)