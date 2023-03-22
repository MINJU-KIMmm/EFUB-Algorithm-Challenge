import sys, copy
from collections import deque

input = sys.stdin.readline
n, L, R = map(int, input().split())

arr = [list(map(int, input().strip().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 이동 시 마다 초기화 하는 값들
temp_arr = [[0]*n for _ in range(n)]
visited = [[0]*n for _ in range(n)]
change = False
def bfs(x, y):
    global change
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    group = []
    group.append((x, y))
    sum_ = arr[x][y]

    while q:
        px, py = q.popleft()

        for i in range(4):
            nx, ny = px+dx[i], py+dy[i]

            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if L<=abs(arr[px][py]-arr[nx][ny])<=R:
                    change = True
                    group.append((nx,ny))
                    sum_ += arr[nx][ny]
                    visited[nx][ny] = 1
                    q.append((nx,ny))

    avg = sum_//len(group)
    for i, j in group:
        temp_arr[i][j] = avg


answer = 0
while True:
    visited = [[0]*n for _ in range(n)]
    temp_arr = [[0]*n for _ in range(n)]
    change = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j)

    # 한번도 안 바뀌었다는 뜻
    if not change:
        break
    else:
        answer += 1
        arr = copy.deepcopy(temp_arr)

print(answer)
