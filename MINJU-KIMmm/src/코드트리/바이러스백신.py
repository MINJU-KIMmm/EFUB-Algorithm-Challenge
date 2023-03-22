import sys, copy
from collections import deque


input = sys.stdin.readline
N, M = map(int, input().split())

arr = [] #0:바이러스, 1:벽, 2:병원
hospital = [] 
virus = []

for i in range(N):
    temp = list(map(int, input().strip().split()))
    for j in range(N):
        if temp[j] == 2:
            hospital.append((i,j))
        if temp[j] == 0:
            virus.append((i,j))
    
    arr.append(temp)


picked = [0 for _ in range(len(hospital))]
answer = sys.maxsize

# 병원 고름
def dfs(depth, start):
    global answer, flag

    if depth == M:
        time = bfs()
        if time != -1:
            answer = min(answer, time)
        return

    for i in range(start, len(hospital)):
        if not picked[i]:
            picked[i] = 1
            dfs(depth+1, i+1)
            picked[i] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 바이러스 없앰
def bfs():
    visited = [[0]*N for _ in range(N)]
    #temp_arr = copy.deepcopy(arr)
    q = deque()
    for i in range(len(picked)):
        if picked[i]:
            q.append((hospital[i][0], hospital[i][1]))
            visited[hospital[i][0]][hospital[i][1]] = 1
    
    max_time = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                if arr[nx][ny]!=1:
                    visited[nx][ny] = visited[x][y]+1
                    if arr[nx][ny]==0:
                        max_time = max(visited[nx][ny], max_time)
                    q.append((nx, ny))

    #print(visited)
    for vx, vy in virus:
        if not visited[vx][vy]:
            return -1
    
    return max_time


dfs(0, 0)
if answer == sys.maxsize:
    print(-1)
elif answer == 0:
    print(answer)
else:
    print(answer-1)
