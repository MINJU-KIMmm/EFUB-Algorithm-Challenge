import heapq

N = int(input())
arr = []

for _ in range(N):
    for n in map(int, input().split()):
        heapq.heappush(arr, n)
    arr = heapq.nlargest(N, arr)

heapq.heapify(arr)
print(heapq.heappop(arr))