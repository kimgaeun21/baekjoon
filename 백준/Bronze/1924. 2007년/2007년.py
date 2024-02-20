
month=[0, 31, 59,90,120,151,181,212, 243,273, 304, 334]

x, y = map(int, input().split())
answer = (month[x-1] + y)%7

day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
print(day[answer])    
    
