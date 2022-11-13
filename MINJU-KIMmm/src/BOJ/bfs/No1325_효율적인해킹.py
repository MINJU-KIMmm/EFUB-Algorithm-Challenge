from collections import deque
import sys

N, M = map(int,sys.stdin.readline().split())
arr = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int,sys.stdin.readline().split())
    arr[B].append(A)

def bfs(start):
    q = deque()
    q.append(start)
    visited = [0 for _ in range(N+1)]
    visited[start] = 1

    count = 1

    while q:
        now = q.popleft()

        for next in arr[now]:
            if not visited[next]:
                q.append(next)
                visited[next] = 1
                count += 1

    return count


max_count = 0
result = []

for i in range(1, N+1):
    cnt = bfs(i)
    max_count = max(max_count, cnt)
    result.append([i, cnt])

for i, cnt in result:
    if cnt == max_count:
        print(i, end=' ')