from itertools import combinations

hobit=[]

for i in range(9):
    hobit.append(int(input()))

arr = combinations(hobit, 7)

for i in arr:
    if sum(i)==100:
        a = list(i)
        for j in sorted(a):
           print(j)
        break;   