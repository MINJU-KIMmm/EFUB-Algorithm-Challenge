N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
answer = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def dfs(depth, sum, x, y):
    global answer
    if depth == 4:
        answer = max(answer, sum)
        return

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
            visited[nx][ny] = 1
            dfs(depth+1, sum+arr[nx][ny], nx, ny)
            visited[nx][ny] = 0

# ㅏ,ㅓ,ㅗ,ㅜ 같은 모양은 상하좌우 이동으로 한번에 가지 못한다.
# 따로 구해줌
def special(x,y):
    global answer
    for i in range(4):
        tmp = arr[x][y]
        for k in range(3):
            idx = (i+k)%4
            nx, ny = x+dx[idx], y+dy[idx]
            if 0<=nx<N and 0<=ny<M:
                tmp += arr[nx][ny]
            else:
                tmp = 0
                break
        answer = max(answer, tmp)

for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(1,arr[i][j],i,j)
        visited[i][j] = 0

        special(i,j)

print(answer)