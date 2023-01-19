import heapq

N = int(input())

_class = [list(map(int, input().split())) for _ in range(N)]
_class.sort()

count = 0
pq = []

for S, T in _class:
    while len(pq) and pq[0][0]<=S:
        heapq.heappop(pq)

    heapq.heappush(pq, (T, S))
    count = max(count, len(pq))

print(count)