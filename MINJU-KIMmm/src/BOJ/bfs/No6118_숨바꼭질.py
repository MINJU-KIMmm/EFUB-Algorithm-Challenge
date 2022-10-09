from collections import deque

N,M = map(int, input().split())
visited = [False]*(N+1)
move = [0]*(N+1)

arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

def bfs():
    q = deque([(1, 0)])
    visited[1] = True

    while q:
        pos, dist = q.popleft()

        for num in arr[pos]:
            if not visited[num]:
                visited[num] = True
                move[num] = dist+1
                q.append((num, dist+1))

bfs()
max_value = max(move)
print(move.index(max_value), max_value, move.count(max_value))