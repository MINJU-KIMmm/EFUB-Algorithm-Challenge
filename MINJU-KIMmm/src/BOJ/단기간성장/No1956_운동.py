import sys
from heapq import heappop, heappush

input = sys.stdin.readline
V, E = map(int, input().split())

connect = [[] for _ in range(V+1)]
pq = []
for _ in range(E):
    a, b, c = map(int, input().split())
    connect[a].append((c, b))
    heappush(pq, [c, a, b])

INF = sys.maxsize
def dijkstra():
    dis_list = [[INF]*(V+1) for _ in range(V+1)]

    while pq:
        c, x, y = heappop(pq)
        if x==y:
            return c
        #print(dis_list)
        if dis_list[x][y] < c:
            continue

        for next_c, next_y in connect[y]:
            if dis_list[x][next_y] > next_c+c:
                dis_list[x][next_y] = next_c+c
                heappush(pq, [next_c+c, x, next_y])


    return -1

print(dijkstra())