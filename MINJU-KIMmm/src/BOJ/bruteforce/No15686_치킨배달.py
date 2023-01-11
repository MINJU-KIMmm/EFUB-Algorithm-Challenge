import sys

N, M = map(int, input().split())
chicken = []
home = []

for i in range(N):
    inputs = list(map(int, input().split()))
    for j in range(N):
        if inputs[j] == 1:
            home.append((i,j))
        elif inputs[j] == 2:
            chicken.append((i,j))


visited = [0]*len(chicken)
answer = sys.maxsize


def dfs(depth, start):
    global answer

    if depth==M:
        total_cost = 0
        for i, j in home:
            cost = sys.maxsize
            for k in range(len(visited)):
                if visited[k]:
                    ci, cj = chicken[k]
                    cost = min(cost, abs(i-ci)+abs(j-cj))
            total_cost += cost
        answer = min(answer, total_cost)
        return

    for i in range(start, len(chicken)):
        visited[i] = 1
        dfs(depth+1, i+1)
        visited[i] = 0


dfs(0, 0)
print(answer)