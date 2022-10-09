from collections import deque
from itertools import combinations

arr = [list(input()) for _ in range(5)]
pos = [(i,j) for i in range(5) for j in range(5)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

combs = list(combinations(pos, 7))


def count_dasom(param_comb):
    count = 0
    for i,j in param_comb:
        if arr[i][j]=='S':
            count += 1

    return True if count>=4 else False


def bfs(param_comb):
    q = deque()
    visited = [False]*7
    q.append(param_comb[0])
    visited[0] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if (nx,ny) in param_comb:
               next = param_comb.index((nx,ny))
               if not visited[next]:
                   visited[next] = True
                   q.append((nx,ny))

    return False if False in visited else True


answer = 0
for comb in combs:
    if count_dasom(comb):
        if bfs(comb):
            answer+=1

print(answer)