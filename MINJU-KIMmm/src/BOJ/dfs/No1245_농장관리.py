

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

dx=[-1,1,0,0,-1,1,-1,1]
dy=[0,0,-1,1,-1,1,1,-1]


count = 0

visited = [[False]*M for _ in range(N)]

def dfs(x, y):
    global peak

    for i in range(8):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<=nx<N and 0<=ny<M:
            if arr[x][y]<arr[nx][ny]:
                peak = False
            if not visited[nx][ny] and arr[nx][ny]==arr[x][y]:
                visited[nx][ny]=True
                dfs(nx,ny)

    return

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            peak = True
            visited[i][j]=True
            dfs(i,j)

            if peak:
                count+=1


print(count)