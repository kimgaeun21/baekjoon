pw = str(input())

    
n = int(input())
dic = []
answer = ''

for i in range(n):
        dic.append(str(input()))

for i in range(26):
    tmp = ''
    for k in pw:
        tmp += chr(((ord(k)-97+i)%26)+97)
    
    for k in dic:
        if k in tmp:
            answer = tmp
    
    if answer != '':
        break
print(answer)
            