from collections import deque

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 0

q = deque()
dist = [[0]*C for _ in range(R)]

def bfs(bx, by):
    while q:
        x, y = q.popleft()
        #도착
        if arr[bx][by]=='S':
            return dist[bx][by]

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0<=nx<R and 0<=ny<C:
                #고슴도치 이동
                if (arr[nx][ny]=='.' or arr[nx][ny]=='D') and arr[x][y]=='S':
                    arr[nx][ny]='S'
                    dist[nx][ny]=dist[x][y]+1
                    q.append((nx,ny))
                #물 이동
                if (arr[nx][ny]=='.' or arr[nx][ny]=='S') and arr[x][y]=='*':
                    arr[nx][ny]='*'
                    q.append((nx,ny))

    return "KAKTUS"


for i in range(R):
    for j in range(C):
        if arr[i][j]=='S':
            q.append((i,j))
        elif arr[i][j]=='D':
            bx, by = i,j

for i in range(R):
    for j in range(C):
        if arr[i][j]=='*':
            q.append((i,j))

print(bfs(bx,by))