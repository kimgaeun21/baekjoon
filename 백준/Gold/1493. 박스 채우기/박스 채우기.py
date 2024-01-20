length, width, height = map(int,input().split())
n = int(input())
cube = {}
for i in range(n):
    a, b = map(int, input().split())
    cube[2**a] = b
    
answer = 0
before = 0

for v in sorted(cube.keys(), reverse=True):
    before *= 8
    max_cnt = (length//v) * (width//v) * (height//v) - before
    max_cnt = min(cube[v], max_cnt)
    answer += max_cnt 
    before += max_cnt
    
if length * width * height == before:
    print(answer)
else:
    print(-1)
