import sys, heapq

input = sys.stdin.readline
N = int(input())
M = int(input())

arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().strip().split())
    arr[a].append((c, b))
    arr[b].append((c, a))


pq = [(0, 1)]
visited = [0 for _ in range(N+1)]
count, answer = 0, 0
while pq:
    if count == N:
        break

    cost, v = heapq.heappop(pq)
    if not visited[v]:
        visited[v] = 1
        answer += cost
        count += 1

        for i in arr[v]:
            heapq.heappush(pq, i)

print(answer)