N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

result = 0
for i in range(len(arr)):
    minData = min(arr[i])
    result = max(minData, result)

print(result)