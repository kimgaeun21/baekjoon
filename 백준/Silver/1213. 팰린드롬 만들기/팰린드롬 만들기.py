import sys
from collections import Counter

x= list(map(str, sys.stdin.readline().strip()))
x.sort()
check=Counter(x)

odd=0
center=""

for i in check:
    if check[i] % 2 != 0:
        odd += 1
        center += i
        x.remove(i)
    
    if odd > 1:
        print("I'm Sorry Hansoo")
        break
    
    
result = ""
if odd <= 1:
    for i in range (0, len(x), 2):
        result += x[i] 
    print(result + center + result[::-1])