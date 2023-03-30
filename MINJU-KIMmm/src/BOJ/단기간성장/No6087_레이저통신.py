import sys
from collections import deque

input = sys.stdin.readline

W, H = map(int, input().split())
arr = [list(input().strip()) for _ in range(H)]
sx, sy, ex, ey = -1, -1, -1, -1

for i in range(H):
    for j in range(W):
        if arr[i][j] == 'C':
            if sx==-1 and sy==-1:
                sx, sy = i, j
            else:
                ex, ey = i, j

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


answer = sys.maxsize

def bfs():
    global answer
    visited = [[sys.maxsize]*W for _ in range(H)]
    q = deque()
    q.append((sx, sy, 4, 0))
    visited[sx][sy] = 0
    visited_cnt = [[0]*W for _ in range(H)]
    visited_cnt[sx][sy] = 1

    while q:
        px, py, dir, cnt = q.popleft()
        if px==ex and py==ey:
            if answer <= cnt:
                continue
            answer = min(answer, cnt)
        for i in range(4):
            nx, ny = px+dx[i], py+dy[i]

            if 0<=nx<H and 0<=ny<W and arr[nx][ny]!='*' and visited_cnt[nx][ny]<W*H:
                #print(nx,ny, H, W)
                if i!=dir:
                    if visited[nx][ny]>=cnt+1:
                        visited[nx][ny] = cnt+1
                        q.append((nx,ny,i,cnt+1))
                        visited_cnt[nx][ny] += 1
                else:
                    if visited[nx][ny]>=cnt:
                        visited[nx][ny] = cnt
                        q.append((nx,ny,i,cnt))
                        visited_cnt[nx][ny] += 1

#print(bfs())
bfs()
#print(mir[ex][ey])
print(answer-1)