from collections import deque

T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0

def bfs(x, y):
    global cnt, visited

    q = deque([(x, y)])
    visited[x][y] = 1

    while q:
        px, py = q.popleft()

        for i in range(4):
            nx, ny = px + dx[i], py + dy[i]

            if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and arr[nx][ny] == '#':
                q.append((nx, ny))
                visited[nx][ny] = 1


for _ in range(T):
    cnt = 0
    H, W = map(int, input().split())
    arr = [list(input()) for _ in range(H)]

    visited = [[0] * W for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if arr[i][j] == '#' and not visited[i][j]:
                bfs(i, j)
                cnt += 1

    print(cnt)
