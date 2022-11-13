from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(n, m, maps):
    visited = [[0] * m for _ in range(n)]
    q = deque([(0, 0)])
    visited[0][0] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] == 1:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

    return visited[n - 1][m - 1] if visited[n - 1][m - 1] else -1


def solution(maps):
    answer = bfs(len(maps), len(maps[0]), maps)
    return answer