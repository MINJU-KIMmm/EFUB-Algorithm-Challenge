from collections import deque
import sys

M, N, H = map(int, input().split())  # 가로, 세로, 상자수

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

arr = []
q = deque()
for i in range(H):
    tmp = []
    for j in range(N):
        tmp.append(list(map(int, sys.stdin.readline().split())))
        for k in range(M):
            if tmp[j][k]==1:
                q.append((i,j,k))
    arr.append(tmp)

while q:
    px, py, pz = q.popleft()
    for i in range(6):
        nx, ny, nz = px + dx[i], py + dy[i], pz + dz[i]

        if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M and arr[nx][ny][nz] == 0:
            q.append((nx, ny, nz))
            arr[nx][ny][nz] = arr[px][py][pz] + 1


day = 0
for i in arr:
    for j in i:
        for k in j:
            if k==0:
                print(-1)
                exit(0)
        day = max(day,max(j))
print(day-1)
