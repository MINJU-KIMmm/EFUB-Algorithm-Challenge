M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

visited = [[False] * N for _ in range(M)]

count = 0

dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]


def bfs(x, y):
    q = []
    q.append([x, y])
    visited[x][y] = True

    while q:
        cur = q.pop()
        px = cur[0]
        py = cur[1]

        for i in range(8):
            nx = px + dx[i]
            ny = py + dy[i]

            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny]==1:
                q.append([nx, ny])
                visited[nx][ny] = True


for i in range(M):
    for j in range(N):
        if arr[i][j] == 1 and not visited[i][j]:
            bfs(i, j)
            count += 1

print(count)