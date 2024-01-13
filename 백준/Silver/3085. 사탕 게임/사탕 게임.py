def check(candy):
    # for i in candy:
    #     print(i)
    max = 0
    
    for i in range(n):
        count = 1
        for j in range(1,n):
            if candy[i][j] == candy[i][j-1]:
                count += 1
                if count > max :
                    max = count
            else:
                if count > max :
                    max = count
                count =1
                
            
        
    for i in range(n):
        count =1 
        for j in range(1,n):
            if candy[j][i] == candy[j-1][i]:
                count += 1
                if count > max :
                    max = count
            else:
                if count > max :
                    max = count
                count =1   

    # print(max)
    return max
            
n= int(input())
candy=[]

for _ in range(n):
    i = list(input())
    candy.append(i)

answer = 0

for i in range(n):
    for j in range(n-1):
        candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
        answer = max(answer, check(candy))
        
        candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
        
        candy[j][i], candy[j+1][i] = candy[j+1][i], candy[j][i]
        answer = max(answer, check(candy))
        
        candy[j][i], candy[j+1][i] = candy[j+1][i], candy[j][i]

print(answer)