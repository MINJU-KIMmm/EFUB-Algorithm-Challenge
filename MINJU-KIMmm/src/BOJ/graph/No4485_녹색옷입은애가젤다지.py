import sys
import heapq
from collections import deque

INF = sys.maxsize
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 가중치가 있는 그래프의 최단거리를 구하는 경우 다익스트라를 사용하는 것이 일반적인 풀이 방
# 만약 음수 경로가 있다면 벨만 포드 알고리즘을 사용해야 한다.
def dijkstra():
    pq = []
    dis_list = [[INF]*N for _ in range(N)]
    dis_list[0][0] = arr[0][0]
    heapq.heappush(pq, [arr[0][0], (0,0)])

    while pq:
        dis, (x,y) = heapq.heappop(pq)

        if dis_list[x][y] < dis:
            continue

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0<=nx<N and 0<=ny<N:
                if dis_list[nx][ny] > dis_list[x][y] + arr[nx][ny]:
                    dis_list[nx][ny] = dis_list[x][y] + arr[nx][ny]
                    heapq.heappush(pq, [dis_list[nx][ny], (nx,ny)])

    return dis_list[N-1][N-1]


def bfs():
    q = deque()
    q.append((0,0))
    visited = [[INF]*N for _ in range(N)]
    visited[0][0] = arr[0][0]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0<=nx<N and 0<=ny<N:
                if visited[nx][ny] > visited[x][y]+arr[nx][ny]:
                    visited[nx][ny] = visited[x][y]+arr[nx][ny]
                    q.append((nx,ny))

    return visited[N-1][N-1]


count = 1
while True:
    N = int(input())
    if not N:
        break

    arr = [list(map(int, input().split())) for _ in range(N)]

    print("Problem",count, end="")
    print(":", dijkstra())
    #print(":", bfs())

    count += 1
