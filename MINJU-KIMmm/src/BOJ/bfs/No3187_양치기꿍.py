from collections import deque

R,C = map(int, input().split())

arr = [list(input().strip()) for _ in range(R)]
v_count = 0
k_count = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

visited = [[False] * C for _ in range(R)]

def bfs(x, y):
    q = deque([(x,y)])
    visited[x][y]=True

    v = 0
    k = 0
    while q:
        px, py = q.popleft()
        if arr[px][py]=='v':
            v+=1
        elif arr[px][py]=='k':
            k+=1

        for i in range(4):
            nx, ny = px+dx[i], py+dy[i]

            if 0<=nx<R and 0<=ny<C and not visited[nx][ny]:
                if arr[nx][ny]!='#':
                    visited[nx][ny]=True
                    q.append((nx,ny))

    return v, k

for i in range(R):
    for j in range(C):
        if arr[i][j]!='#' and not visited[i][j]:
            v, k = bfs(i,j)
            if v>=k:
                v_count += v
            else:
                k_count += k

print(k_count,v_count)