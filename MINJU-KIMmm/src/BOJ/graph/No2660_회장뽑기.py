import sys

n = int(input())

INF = sys.maxsize

arr = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    arr[i][i]=0

while True:
    a, b = map(int, input().split())
    if a==-1 and b==-1:
        break

    arr[a][b]=1
    arr[b][a]=1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            arr[i][j] = min(arr[i][j], arr[i][k]+arr[k][j])

scores = [0]
score = INF
cand = []
for i in range(1, n+1):
    temp = 0
    arr[i].sort(reverse=True)
    for j in range(1, n+1):
        if arr[i][j]!=INF:
            temp = arr[i][j]
            break

    scores.append(temp)

    score = min(score, temp)


for i in range(1, n+1):
    if scores[i]==score:
        cand.append(i)

print(score, len(cand), sep = " ")
print(*cand)