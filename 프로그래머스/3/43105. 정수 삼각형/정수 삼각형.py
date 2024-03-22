def solution(triangle):
    answer = 0
    if len(triangle) == 1:
        return triangle[0][0]
    elif len(triangle) == 2:
        return (max(triangle[1])+triangle[0])
    else:
        for i in range(len(triangle[1])):
            triangle[1][i] += triangle[0][0]
            
        for i in range(2, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] += triangle[i-1][j]
                elif j == len(triangle[i])-1:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
        return max(triangle[-1])
    return answer