while 1:
    try :
        x, y = input().split()
        
        cnt = 0
        idx= 0
        for i in y:
            if i == x[idx]:
                idx += 1  
            if idx == len(x):
                break
        if idx == len(x):
            print('Yes')
        else:
            print('No')
    except:
        break