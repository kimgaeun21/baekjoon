from itertools import permutations
n, m = map(int, input().split())

combi = permutations(range(1,n+1),m)
for i in combi:
    print(*i)