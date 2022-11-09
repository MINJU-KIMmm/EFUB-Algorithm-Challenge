N, M = map(int, input().split())
arr = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)


answer = False
visited = [False] * N


def dfs(depth, last):
    global answer
    visited[last] = True

    if depth == 5:
        answer = True
        return

    for next in arr[last]:
        if not visited[next]:
            visited[next] = True
            dfs(depth + 1, next)
            visited[next] = False


for i in range(N):
    dfs(1, i)
    visited[i] = False
    if answer:
        break


if answer:
    print(1)
else:
    print(0)



