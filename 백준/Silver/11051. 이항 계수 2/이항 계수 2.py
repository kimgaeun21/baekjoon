n, k = map(int, input().split())
factorial=[1 for _ in range(n+1)]

for i in range(1,n+1):
    factorial[i] = i * factorial[i-1]

print((factorial[n]//(factorial[n-k]*factorial[k]))%10007)

