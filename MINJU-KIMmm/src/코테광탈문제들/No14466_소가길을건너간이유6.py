import sys
from collections import deque

input = sys.stdin.readline
N, K, R = map(int, input().split())

path = [[[] for _ in range(N+1)] for _ in range(N+1)]
for _ in range(R):
    r1, c1, r2, c2 = map(int, input().split())
    path[r1][c1].append((r2, c2))
    path[r2][c2].append((r1, c1))

arr = [[0]*(N+1) for _ in range(N+1)]
cow = []
for _ in range(K):
    x, y = map(int, input().split())
    arr[x][y] += 1
    cow.append((x,y))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = (K*(K-1))//2

cow_visited = [[0]*K for _ in range(K)] # 각 소가 각 소를 방문했는지
# path이용하지 않고 갈 수 있는 곳 구하기
def bfs(x, y, idx):
    global answer
    q = deque()
    q.append((x, y))
    visited = [[0]*(N+1) for _ in range(N+1)]
    visited[x][y] = 1

    while q:
        px, py = q.popleft()
        for i in range(4):
            nx, ny = px+dx[i], py+dy[i]
            if 1<=nx<N+1 and 1<=ny<N+1 and not visited[nx][ny]:
                #길 안 건너도 갈 수 있나?
                if (nx,ny) not in path[px][py]:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                    # 소가 있던 곳이면
                    if arr[nx][ny] > 0:
                        n_idx = cow.index((nx,ny))
                        if not cow_visited[idx][n_idx]:
                            cow_visited[idx][n_idx] = 1
                            cow_visited[n_idx][idx] = 1
                            answer -= 1

    #print(visited)

for i in range(K):
    x, y = cow[i]
    bfs(x, y, i)

#print(cow_visited)
print(answer)

