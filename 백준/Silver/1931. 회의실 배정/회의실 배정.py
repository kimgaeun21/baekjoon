n = int(input())
arr= []

for i in range(n):
    arr.append(list(map(int, input().split())))
    
arr.sort(key=lambda x : (x[1],x[0]))

answer = []
answer.append(arr[0])

for i in arr[1:]:
    if i[0] >= answer[len(answer)-1][1]:
        answer.append(i)
        arr.remove(i)

print(len(answer))