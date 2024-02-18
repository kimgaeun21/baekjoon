n=int(input())
num = set(map(int,input().split()))
m = int(input())
sanggun = list(map(int,input().split()))

for i in range(m):
    if sanggun[i] in num:
        print(1, end=' ')
    else: 
        print(0, end=' ')