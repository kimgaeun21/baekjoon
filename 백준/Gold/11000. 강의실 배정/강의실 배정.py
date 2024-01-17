import sys, heapq
n = int(input())
input = sys.stdin.readline

arr=[]
for i in range(n):
    arr.append(list(map(int, input().split())))
    
arr.sort(key= lambda x: (x[0],x[1]))

answer = []
heapq.heappush(answer, arr[0][1])

for i in arr[1:]:
    if i[0] < answer[0]:
        heapq.heappush(answer, i[1])
    else:
        heapq.heappop(answer)
        heapq.heappush(answer,i[1])
        
print(len(answer))
    