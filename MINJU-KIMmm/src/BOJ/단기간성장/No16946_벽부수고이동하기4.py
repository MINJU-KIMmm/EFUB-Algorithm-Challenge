import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())

blank = []
wall = []
arr = []

for i in range(N):
    temp = list(input().strip())
    for j in range(M):
        if temp[j]=='1':
            wall.append((i,j))
        else:
            blank.append((i,j))

    arr.append(temp)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0]*M for _ in range(N)]
group_num = 1
dic = {}
zero_group = [[0]*M for _ in range(N)]

def bfs(x, y):
    global group_num,zero_group

    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    count = 1
    zero_group[x][y] = group_num

    while q:
        px, py = q.popleft()

        for i in range(4):
            nx, ny = px+dx[i], py+dy[i]
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
                if arr[nx][ny] == '0':
                    zero_group[nx][ny] = group_num
                    visited[nx][ny] = 1
                    count += 1
                    q.append((nx,ny))

    dic[group_num] = count


def update(x, y):
    zero_type = set()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]

        if 0<=nx<N and 0<=ny<M:
            if arr[nx][ny]=='0':
                zero_type.add(zero_group[nx][ny])

    count = 1
    for g in zero_type:
        count += dic[g]
        count%=10

    return count

# 제로 그룹 구하기
for i, j in blank:
    if not visited[i][j]:
        bfs(i, j)
        group_num += 1

new_arr = [[0]*M for _ in range(N)]
for i, j in wall:
    new_arr[i][j] = update(i, j)

for i in range(N):
    for j in range(M):
        print(new_arr[i][j], end='')
    print()