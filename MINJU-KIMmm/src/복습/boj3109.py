import sys

input = sys.stdin.readline

R, C = map(int, input().split())
arr = [list(input().strip()) for _ in range(R)]

answer = 0

visited = [[0]*C for _ in range(R)]
dx = [-1, 0, 1] # 위로 먼저 이동해서 최대한 위로 위치시킴

def dfs(x, y):
    if y==C-1:
        return True

    for i in range(3):
        nx = x+dx[i]
        ny = y+1

        if 0<=nx<R and 0<=ny<C and not visited[nx][ny]:
            if arr[nx][ny]!='x':
                visited[nx][ny] = 1
                if dfs(nx, ny):
                    return True
#                visited[nx][ny] = 0 어차피 위에 애가 못간 경로면 못간다

    return False

for start in range(R):
    if dfs(start, 0):
        answer += 1

print(answer)