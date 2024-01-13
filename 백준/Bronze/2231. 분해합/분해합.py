x = int(input())
answer = 0
for i in range(x):
    tmp = i
    for j in str(i):
        tmp += int(j)
    if tmp == x:
        answer = i
        break

print(answer)