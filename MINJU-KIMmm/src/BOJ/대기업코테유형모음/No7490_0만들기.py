import sys

input = sys.stdin.readline
T = int(input())

def dfs(depth, result, calc, before, N, concat):
    if depth == N:
        if result == 0:
            answer.append(calc)
        return

    for i in range(3):
        if i==1:
            if not visited[depth][i]:
                visited[depth][i] = 1
                dfs(depth+1, result+depth+1, calc+'+'+str(depth+1), '+', N, depth+1)
                visited[depth][i] = 0

        if i==2:
            if not visited[depth][i]:
                visited[depth][i] = 1
                dfs(depth+1, result-depth-1, calc+'-'+str(depth+1), '-', N, depth+1)
                visited[depth][i] = 0

        if i==0:
            if not visited[depth][i]:
                visited[depth][i] = 1
                if before=='-':
                    dfs(depth+1, result+concat-(concat*10+(depth+1)), calc+' '+str(depth+1), '-',N, concat*10+(depth+1))
                else:
                    dfs(depth+1, result-concat+(concat*10+(depth+1)), calc+' '+str(depth+1), '+',N, concat*10+(depth+1))
                visited[depth][i] = 0

for _ in range(T):
    num = int(input())
    visited = [[0]*3 for _ in range(num+1)]
    answer = []
    dfs(1, 1, '1', '', num, 1)
    answer.sort()
    for a in answer:
        print(a)

    print()