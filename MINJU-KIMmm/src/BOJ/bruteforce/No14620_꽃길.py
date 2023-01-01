import sys

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

answer = sys.maxsize
cost = 0

visited = [[0]*N for _ in range(N)]
dx = [0,-1,1,0,0]
dy = [0,0,0,-1,1]


def visit_check(x, y):
    for k in range(5):
        nx, ny = x+dx[k], y+dy[k]
        if visited[nx][ny]:
            return False

    return True


def plant(depth):
    global answer, cost

    if depth==3:
        answer = min(answer, cost)
        return

    for i in range(1, N-1):
        for j in range(1, N-1):
            if visit_check(i,j):
                for k in range(5):
                    nx = i+dx[k]
                    ny = j+dy[k]

                    visited[nx][ny] = 1
                    cost += arr[nx][ny]

                plant(depth+1)

                for k in range(5):
                    nx = i+dx[k]
                    ny = j+dy[k]

                    visited[nx][ny] = 0
                    cost -= arr[nx][ny]


plant(0)
print(answer)

