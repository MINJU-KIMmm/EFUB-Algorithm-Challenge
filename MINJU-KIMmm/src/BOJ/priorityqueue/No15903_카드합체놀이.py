import heapq

n, m = map(int, input().split())

arr = list(map(int, input().split()))
heapq.heapify(arr)

for _ in range(m):
    first = heapq.heappop(arr)
    second = heapq.heappop(arr)

    sum = first + second
    heapq.heappush(arr, sum)
    heapq.heappush(arr, sum)

total = 0
for num in arr:
    total += num

print(total)