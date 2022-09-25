N = int(input())

INF = 1e9
arr = [list(input().strip()) for _ in range(N)]
floyd = [[INF]*N for _ in range(N)]
result = [0 for _ in range(N)]

for i in range(N):
    floyd[i][i]=0
    for j in range(N):
        if arr[i][j] == 'Y':
            floyd[i][j] = 1


for k in range(N):
    for i in range(N):
        for j in range(N):
            floyd[i][j] = min(floyd[i][j], floyd[i][k]+floyd[k][j])

for i in range(N):
    for j in range(N):
        if 0<floyd[i][j]<=2:
            result[i]+=1

print(max(result))


