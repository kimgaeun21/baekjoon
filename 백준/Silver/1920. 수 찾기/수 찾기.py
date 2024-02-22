

n = int(input())
n_arr = list(map(int, input().split()))
n_arr.sort()

m = int(input())
m_arr = list(map(int, input().split()))

def find(a):
    start = 0 
    end =n -1
    
    while start <= end:
        mid = (start+end)//2
        if  n_arr[mid] == a:
            return 1
        elif n_arr[mid] < a:
            start = mid+1
        else:
            end = mid-1
    return 0        
        
for i in m_arr:
    print(find(i))
    
