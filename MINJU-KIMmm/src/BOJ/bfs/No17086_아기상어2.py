from collections import deque

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]

result = 0


dist = [[0] * M for _ in range(N)]


def bfs(x, y):
    q = deque([(x, y)])
    visited = [[False] * M for _ in range(N)]
    visited[x][y] = True

    while q:
        px, py = q.popleft()

        for i in range(8):
            nx, ny = px + dx[i], py + dy[i]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if arr[nx][ny] == 0:
                    q.append((nx, ny))
                    dist[nx][ny] = dist[px][py]+1 if not dist[nx][ny] else min(dist[px][py]+1, dist[nx][ny])

                    visited[nx][ny] = True


for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            bfs(i, j)


print(max(map(max, dist)))