
def check(tmp):
    arr = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']
    cnt = 0
    
    for i in range(8):
        for j in range(8):
            if arr[i][j] != tmp[i][j]:
                cnt += 1
    
    return min(cnt, 64-cnt)

n, m = map(int, input().split())
chess=[]
answer =123456789

for i in range(n):
    chess.append(input())
    

for i in range(n-7):
    for j in range(m-7):
        tmp=[]
        for k in range(8):
            tmp.append(chess[i+k][j:j+8])
        answer = min(answer, check(tmp))

print(answer)