N, K = map(int, input().split())

A = list(map(int, input().split()))

cnt = 0
visited = [0]*N


def dfs(depth, num):
    global cnt
    if depth == N:
        cnt += 1

    for i in range(N):
        if num-K+A[i] >= 500 and not visited[i]:
            visited[i] = 1
            dfs(depth+1, num-K+A[i])
            visited[i] = 0


dfs(0, 500)
print(cnt)