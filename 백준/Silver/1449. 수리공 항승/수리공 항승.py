n, l = map(int, input().split())

arr= list(map(int, input().split()))
arr.sort()
start = 0
rear = 0
answer = 0

while rear < n:
    if arr[rear] - arr[start] + 1 <= l:
        rear += 1
        continue
    else:
        start = rear
        answer += 1

print(answer+1)