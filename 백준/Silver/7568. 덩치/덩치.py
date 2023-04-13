n = int(input())
array=[]

for i in range(n):
    array.append(list(map(int, input().split())))

for i in range(n):
    tmp=1
    for j in range(n):
        if array[i][0] < array[j][0] and array[i][1]< array[j][1]:
            tmp = tmp + 1

    print(str(tmp), end =" ")
