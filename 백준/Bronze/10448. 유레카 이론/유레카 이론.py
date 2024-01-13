from itertools import combinations_with_replacement

arr = [int(i*(i+1)/2) for i in range(1,44)]
# print(arr)

a = list(combinations_with_replacement(arr,3))


n = int(input())
for i in range(n):
    x = int(input())
    answer = 0
    for j in a:
        if sum(j) == x:
            answer = 1
            break
    print(answer)
