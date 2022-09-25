from collections import deque

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

visited = [[False]*M for _ in range(N)]
count = 0


def bfs(x, y):
    q = deque([(x,y)])
    visited[x][y]=True

    while q:
        px, py = q.popleft()
        if arr[px][py]=='-':
            if py+1<M and not visited[px][py+1] and arr[px][py+1]=='-':
                visited[px][py+1]=True
                q.append((px, py+1))

        elif arr[px][py]=='|':
            if px+1<N and not visited[px+1][py] and arr[px+1][py]=='|':
                visited[px+1][py]=True
                q.append((px+1,py))


for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            bfs(i,j)
            count+=1

print(count)


