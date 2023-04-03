# 다익스트라
import sys
from heapq import heappush, heappop

input = sys.stdin.readline
N, M = map(int, input().split())

connect = [[] for _ in range(N+1)]
INF = sys.maxsize

for _ in range(M):
    a, b, c = map(int, input().split())
    connect[a].append((c, b))
    connect[b].append((c, a))

#print(connect)
def dijkstra(start, end):
    dis_list = [INF for _ in range(N+1)]
    pq = []

    dis_list[start] = 0
    heappush(pq, (0, start))

    while pq:
        cost, node = heappop(pq)

        if dis_list[node] < cost:
            continue

        #print(connect[node][0])
        for (nc, nx) in connect[node]:
            if dis_list[nx] > nc+cost:
                dis_list[nx] = nc+cost
                heappush(pq, (dis_list[nx], nx))

    return dis_list[end]


print(dijkstra(1, N))
