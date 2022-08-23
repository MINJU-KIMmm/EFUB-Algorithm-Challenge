n = int(input())
m = int(input())
INF = 1e9
count = 0

arr = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    arr[i][i]=0

for i in range(m):
    a, b = map(int, input().split())
    arr[a][b]=1
    arr[b][a]=1

count = 0
for i in range(n+1):
    for b in range(n+1):
        arr[1][b]=min(arr[1][i]+arr[i][b], arr[1][b])

for i in range(n+1):
    if 1<=arr[1][i]<=2:
        count+=1

print(count)