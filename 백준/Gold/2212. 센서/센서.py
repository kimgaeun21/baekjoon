n = int(input())
k = int(input())

senser = list(map(int, input().split()))
senser.sort()

arr=[]

for i in range(1,len(senser)):
   arr.append(senser[i]-senser[i-1])
    
arr.sort()

print(sum(arr[:n-k]))