n = int(input())
if n < 100:
    print (n)
else:
    answer = 99
    for i in range(100,n+1):
        st_i = str(i)
        dx = int(st_i[0])-int(st_i[1])
        for j in range(len(st_i)-1):
            if dx != int(st_i[j]) - int(st_i[j+1]):
                break
            if j == len(st_i)-2:
                answer = answer + 1

    print (answer)