from collections import deque
M, N = map(int, input().split())

arr = [list(map(int, input())) for _ in range(M)]
visited = [[0]*N for _ in range(M)]
q = deque()

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():

    while q:
        px, py = q.popleft()
        if px==(M-1):
            return "YES"

        for i in range(4):
            nx, ny = px+dx[i], py+dy[i]

            if 0<=nx<M and 0<=ny<N and not visited[nx][ny]:
                if arr[nx][ny]==0:
                    visited[nx][ny]=True
                    q.append((nx,ny))

    return "NO"


for i in range(N):
    if arr[0][i]==0:
        q.append((0,i))
        visited[0][i] = True


print(bfs())