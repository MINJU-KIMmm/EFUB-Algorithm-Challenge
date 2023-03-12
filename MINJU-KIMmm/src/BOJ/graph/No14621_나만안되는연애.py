import sys, heapq

# 최소 스패닝 트리
# 프림 알고리즘

# [모든 정점을 연결]하는 [최단 거리]를 찾기 위해 최소 스패닝 트리 알고리즘을 사용한다.

input = sys.stdin.readline
N, M = map(int, input().split())
school = list(input().strip().split())
connect = [[] for _ in range(N)]

for _ in range(M):
    u, v, d = map(int, input().split())
    connect[u-1].append([d, v-1])
    connect[v-1].append([d, u-1])

visited = [0 for _ in range(N)]
ans, cnt = 0, 0
pq = []
pq.append([0, 0]) #거리, 번호

while pq:
    if cnt==N:
        break

    cost, node = heapq.heappop(pq)
    type = school[node]

    if not visited[node]:
        ans += cost
        visited[node] += 1
        cnt += 1

        for n_cost, n_node in connect[node]:
            # 각 학교 성별이 다를 때만 큐에 삽입
            if school[n_node] != school[node]:
                heapq.heappush(pq, [n_cost, n_node])

#print(visited)
if 0 in visited:
    print(-1)
else:
    print(ans)
