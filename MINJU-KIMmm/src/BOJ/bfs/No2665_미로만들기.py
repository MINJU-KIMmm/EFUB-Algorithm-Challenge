from collections import deque

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
q = deque()
dx = [-1,1,0,0]
dy = [0,0,-1,1]
dist = [[-1]*n for _ in range(n)] #지금 경로에 있는 검은방 개수 세기 & 방문확인 용도


def bfs():
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0<=nx<n and 0<=ny<n and dist[nx][ny]==-1:
                if arr[nx][ny]==0:
                    q.append((nx,ny))
                    dist[nx][ny]=dist[x][y]+1
                else:
                    q.appendleft((nx,ny)) #흰방에 우선적으로 방문하도록 appendleft
                    dist[nx][ny]=dist[x][y]

dist[0][0]=0
q.append((0,0))
bfs()
print(dist[n-1][n-1])