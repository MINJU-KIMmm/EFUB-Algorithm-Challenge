import sys

N, M = map(int, input().split())
chicken = []
home = []
answer = sys.maxsize

for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j]==1:
            home.append((i,j))
        elif temp[j]==2:
            chicken.append((i,j))


open = [0]*len(chicken)


def dfs(start, depth):
    global answer
    if depth==M:
        total = 0
        for i in range(len(home)):
            r1, c1 = home[i]
            dist = sys.maxsize
            for j in range(len(chicken)):
                if open[j]:
                    r2, c2 = chicken[j]
                    dist = min(dist, abs(r1-r2)+abs(c1-c2))

            total += dist

        answer = min(answer, total)
        return

    for i in range(start, len(chicken)):
        open[i] = 1
        dfs(i+1, depth+1)
        open[i] = 0

dfs(0, 0)
print(answer)
