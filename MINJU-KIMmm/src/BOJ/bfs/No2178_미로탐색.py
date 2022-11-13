from collections import deque

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    q = deque([(0,0)])
    visited[0][0] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
                if arr[nx][ny]=='1':
                    q.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1


bfs()

print(visited[N-1][M-1])