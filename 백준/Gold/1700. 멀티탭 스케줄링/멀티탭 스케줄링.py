n, k= map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
multitap=[]

for i in range(len(arr)):
    
    if len(multitap) < n:
        if arr[i] in multitap:
            continue
        
        multitap.append(arr[i])
    
    else:
        indexs=[]
        for j in multitap:
            if j in arr[i:]:
                indexs.append(arr[i:].index(j))
            else: 
                indexs.append(999)
            
        if arr[i] in multitap:
            continue
        else:
            multitap.pop(indexs.index(max(indexs)))
            answer += 1
            multitap.append(arr[i])

print(answer)
