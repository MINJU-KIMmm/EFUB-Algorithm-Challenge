from collections import deque

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, cost = map(int, input().split())
    arr[a].append((b, cost))
    arr[b].append((a, cost))


def bfs(start, end):
    q = deque([(start, 0)]) #노드 정보, start로부터 거리
    visited = [0]*(N+1)
    visited[start] = 1

    while q:
        node, dist = q.popleft()

        if node == end:
            return dist
        for next,d in arr[node]:
            if not visited[next]:
                visited[next] = 1
                q.append((next, dist+d))

for _ in range(M):
    a, b = map(int, input().split())
    print(bfs(a,b))