x = int(input())
line = 0
max = 0
while x > max:
    line = line + 1
    max = max + line

n =  max - x
if (line%2 == 0):
    top = line - n 
    bottom = line - top + 1
else:
    bottom = line - n
    top = line - bottom + 1

print('{}/{}'.format(top, bottom))
