import sys


input = sys.stdin.readline
N = int(input())

arr = [0]+[int(input()) for _ in range(N)]

visited = [0 for _ in range(N+1)]

def dfs(n):
    num = arr[n]
    if not visited[num]:
        visited[num] = 1
        up.add(n)
        down.add(num)
        dfs(num)

answer = []
for n in range(1, N+1):
    up = set()
    down = set()

    dfs(n)
    if up==down:
        for x in down:
            answer.append(x)
    else:
        for x in down:
            visited[x] = 0

print(len(answer))
answer.sort()
for a in answer:
    print(a)