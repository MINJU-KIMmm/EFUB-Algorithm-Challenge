import sys
import heapq

input = sys.stdin.readline
n,m = map(int, input().split())

a = list(map(int, input().strip().split()))

# ㄱㅏ장 작게 만드려면? -> 항상 가장 작은 2개의 수끼리 더해줘야 한다. -> pq 사용
pq = []
for num in a:
    heapq.heappush(pq, num)

for _ in range(m):
    new = heapq.heappop(pq)+heapq.heappop(pq)
    heapq.heappush(pq, new)
    heapq.heappush(pq, new)

print(sum(pq))