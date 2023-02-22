import sys

input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = sys.maxsize
visited = [0]*N
result = []


def dfs(depth, start, k):
    if depth == k:
        temp = []
        for i in range(N):
            if visited[i]:
                temp.append(i)
        result.append(temp)
        return

    for i in range(start, N):
        if not visited[i]:
            visited[i] = 1
            dfs(depth+1, i+1, k)
            visited[i] = 0


for i in range(1, N+1):
    dfs(0, 0, i)

for i in range(len(result)):
    mul = 1
    sum = 0

    for j in result[i]:
        mul *= arr[j][0]
        sum += arr[j][1]

    answer = min(answer, abs(mul-sum))

print(answer)