n = int(input())
homework={}

for i in range(n):
    x, y =  map(int, input().split())
    if x in homework.keys():
        homework[x].append(y)
    else:
        homework[x]=[]
        homework[x].append(y)

arr = sorted(homework.keys())
answer = []
for i in arr:
    answer = answer + homework[i]
    answer.sort(reverse=True)
    answer = answer[:i]

print(sum(answer))