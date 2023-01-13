import sys, copy
from collections import deque

N, Q = map(int, input().split())
arr = [[] for _ in range(N+1)]

for _ in range(N-1):
    p, q, r = map(int, input().split())

    arr[p].append((q, r))
    arr[q].append((p,r))


def bfs(start, k):
    visited = [0]*(N+1)
    visited[start] = 1

    q = deque()
    q.append((start, sys.maxsize))

    count = 0
    while q:
        now_node, now_cost = q.popleft()

        for next_node, next_cost in arr[now_node]:
            if not visited[next_node]:
                min_cost = min(now_cost, next_cost)
                q.append((next_node, min_cost))
                if min_cost >= k:
                    count += 1
                visited[next_node] = 1

    return count


for _ in range(Q):
    k, v = map(int, input().split())
    print(bfs(v, k))




