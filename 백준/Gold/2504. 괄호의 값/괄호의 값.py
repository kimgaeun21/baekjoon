def divandmerge(answer):
    count=0
    
    if len(answer)==1:
        if answer[0][0] =='(':
            return 2
        else:
            return 3
    
    mini = min(answer,key=lambda x:x[1])
    check= mini[1]
    tmp=[]

    for i in answer:
        if i[1] != check:
            tmp.append(i)
        else:
            if i[0] == '(':
                if tmp !=[]:
                    x = divandmerge(tmp)
                    count += x*2
                else:
                    count += 2
            elif i[0] =='[':
                if tmp !=[]:
                    x = divandmerge(tmp)
                    count += x*3
                else:
                    count += 3
            tmp=[]
    return count

                
arr = input()
answer = []
stack = []

for i in arr:
    
    if i == '(' or i == '[':
        stack.append(i)
    elif i ==')':
        if stack != [] and stack[-1]=='(':
            answer.append([stack.pop(-1),len(stack)])
        else:
            stack.append(i)
    elif i ==']':
        if stack !=[] and stack[-1]=='[':
            answer.append([stack.pop(-1),len(stack)])
        else:
            stack.append(i)

if len(stack) != 0:
    print(0)
else:
    print(divandmerge(answer))    
