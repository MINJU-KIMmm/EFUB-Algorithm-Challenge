from collections import deque
from itertools import combinations
import sys

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
q = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = sys.maxsize

def bfs(v):
    q = deque(v)
    visited = [[-1]*N for _ in range(N)]
    cnt = 0
    for x,y in q:
        visited[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==-1:
                if arr[nx][ny]!=1:
                    visited[nx][ny]=visited[x][y]+1
                    cnt = max(cnt, visited[nx][ny])
                    q.append((nx,ny))

    for i in range(N):
        for j in range(N):
            if arr[i][j]==0 and visited[i][j]==-1:
                return sys.maxsize

    return cnt


#바이러스 좌표 저장
virus = []
for i in range(N):
    for j in range(N):
        if arr[i][j]==2:
            virus.append([i,j])

#바이러스 좌표로 조합. 조합 경우의 수에 따라 bfs
for v in combinations(virus, M):
    answer = min(bfs(v), answer)

if answer==sys.maxsize:
    print(-1)
else:
    print(answer)