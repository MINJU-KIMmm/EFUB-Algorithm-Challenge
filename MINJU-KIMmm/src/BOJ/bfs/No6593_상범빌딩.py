from collections import deque

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

def bfs(x, y, z):
    q.append((x,y,z))
    cost[x][y][z]=1

    while q:
        px,py,pz = q.popleft()

        for i in range(6):
            nx,ny,nz = px+dx[i], py+dy[i], pz+dz[i]

            if 0<=nx<L and 0<=ny<R and 0<=nz<C and not cost[nx][ny][nz]:
                if arr[nx][ny][nz]=='E':
                    print("Escaped in {0} minute(s).".format(cost[px][py][pz]))
                    return
                if arr[nx][ny][nz]=='.':
                    q.append((nx,ny,nz))
                    cost[nx][ny][nz]=cost[px][py][pz]+1

    print("Trapped!")
    return


# #:막힘 / .:빈칸 / S:시작 / E:탈출
while(True):
    L, R, C = map(int, input().split())
    if L==0 and R==0 and C==0:
        break

    arr = [[[]*C for _ in range(R)] for _ in range(L)]
    cost = [[[0]*C for _ in range(R)] for _ in range(L)]
    q = deque()

    for i in range(L):
        arr[i] = [list(map(str, input().strip())) for _ in range(R)]
        input()

    for i in range(L):
        for j in range(R):
            for k in range(C):
                if arr[i][j][k]=='S':
                    bfs(i,j,k)