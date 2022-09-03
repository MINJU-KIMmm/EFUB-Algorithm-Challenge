N, L = map(int, input().split())

n = 0
x = 0
count = 0

for i in range(L, 101):
    x = (i-1)*i/2
    if (N-x)%i==0 and (N-x)/i>=0:
        n = (int)((N-x)/i)
        count = i
        break

if count==0:
    print(-1)
else:
    for i in range(count):
        print(n+i, end=" ")