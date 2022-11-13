from collections import deque
import sys

N,M,R = map(int,sys.stdin.readline().split())
arr = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int,sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(1, N+1):
    arr[i].sort()

visited = [0 for _ in range(N+1)]

def bfs():
    visited[R] = 1
    q = deque()
    q.append(R)
    val = 1

    while q:
        node = q.popleft()
        for next in arr[node]:
            if not visited[next]:
                val += 1
                visited[next] = val
                q.append(next)


bfs()

for i in range(1, N+1):
    print(visited[i])