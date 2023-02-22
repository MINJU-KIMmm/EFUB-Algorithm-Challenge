import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int, input().split())
# arr = [[0 for _ in range(M)] for _ in range(N)]
#ice = []

arr = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
time = 0


# def melt():
#     melt_list = []
#     for i in range(N):
#         for j in range(M):
#             for d in range(4):
#                 nx, ny = i+dx[d], j+dy[d]
#
#                 if 0<=nx<N and 0<=ny<M and not arr[nx][ny]:
#                     melt_list.append((i,j))
#
#     for i, j in melt_list:
#         arr[i][j] = max(arr[i][j]-1, 0)



visited = [[0]*M for _ in range(N)]


def bfs(x, y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1

    melting = []

    while q:
        px, py = q.popleft()
        melt_cnt = 0
        for i in range(4):
            nx, ny = px+dx[i], py+dy[i]

            if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
                if arr[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                else:
                    melt_cnt += 1
        if melt_cnt:
            melting.append((px, py, melt_cnt))

    return melting


count = 0


while True:
    count = 0
    visited = [[0]*M for _ in range(N)]
    for i in range(1, N-1):
        for j in range(1, M-1):
            if not visited[i][j] and arr[i][j]!=0:
                melting = bfs(i, j)
                count += 1

    for mx, my, melt_cnt in melting:
        arr[mx][my] = max(0, arr[mx][my]-melt_cnt)

    if count == 0:
        time = 0
        break
    if count >= 2:
        break

    time += 1

print(time)