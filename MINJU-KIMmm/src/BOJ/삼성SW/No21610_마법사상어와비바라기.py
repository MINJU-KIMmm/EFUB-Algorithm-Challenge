import copy
import sys

input = sys.stdin.readline

N,M = map(int, input().split())
A = [list(map(int, input().strip().split())) for _ in range(N)] #물
move = [list(map(int, input().strip().split())) for _ in range(M)] #이

dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

# cloud = [[0 for _ in range(N)] for _ in range(N)]
# cloud[N-1][0] = 1
# cloud[N-1][1] = 1
# cloud[N-2][0] = 1
# cloud[N-2][1] = 1

cloud_pos = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]
def cloud_move(m):
    global cloud_pos
    d, s = move[m]
    # for x in range(N):
    #     for y in range(N):
    # print(d, s)
    new_cloud_pos = []

    for x, y in cloud_pos:
        # nx = (x + dx[d] * s) % N
        # ny = (y + dy[d] * s) % N
        nx = x
        ny = y

        for _ in range(s):
            nx = nx+dx[d]
            ny = ny+dy[d]

            if nx>=N:
                nx = N-nx
            if ny>=N:
                ny = N-ny
            if nx<0:
                nx = N+nx
            if ny<0:
                ny = N+ny

        new_cloud_pos.append((nx, ny))

    cloud_pos = copy.deepcopy(new_cloud_pos)
#    cloud_pos = new_cloud_pos

#2, 3
def rain():
    global cloud_pos
    before_cloud = copy.deepcopy(cloud_pos)
    before_visited = [[0]*N for _ in range(N)]
    for x, y in cloud_pos:
        A[x][y] += 1
        before_visited[x][y] = 1

    cloud_pos = []
    return before_cloud, before_visited

#4, 5
ddx = [-1, 1, -1, 1]
ddy = [-1, 1, 1, -1]
def magic(before_cloud, visited):
    for x, y in before_cloud:
        count = 0
        for i in range(4):
            nx = x+ddx[i]
            ny = y+ddy[i]

            if 0<=nx<N and 0<=ny<N:
                if A[nx][ny]>0:
                    count += 1

        A[x][y] += count

    for i in range(N):
        for j in range(N):
            if A[i][j]>=2:
                if (i, j) not in before_cloud  and A[i][j]>=2:
                    A[i][j]-=2
                    cloud_pos.append((i,j))

for m in range(M):
    cloud_move(m)
    before, visited = rain()
    magic(before, visited)

water = 0
for i in range(N):
    for j in range(N):
        water += A[i][j]

print(water)