n = list(str(input()))
pw = str(input())
n_sort = sorted(n)
pw_arr=[[n_sort[i]] for i in range(len(n))]

x = len(pw)//len(n)
for i in range(len(pw)):
    pw_arr[i//x].append(pw[i])
        

arr = []

for i in n:
    for j in range(len(n)):
        if pw_arr[j][0] == i:
            x = []
            for k in pw_arr[j]:
                x.append(k)
            arr.append(x)
            pw_arr[j].insert(0,'*')
            break

for i in range(1,len(arr[0])):
    for j in range(len(arr)):
        print(arr[j][i], end ='')
    
        
        

            
    

