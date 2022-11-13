from collections import deque

W, H = map(int, input().split())
arr = [[0 for _ in range(W+2)] for _ in range(H+2)] # 빈칸을 기준으로 맞닿아 있는 벽면의 개수를 세기 위해 빈칸으로 배열을 감싸준다
for i in range(1, H+1):
    arr[i][1:W+1] = map(int, input().split())

dy = [-1, 1, 0, 0, -1, 1]
dx = [[0,0,-1,1,-1,-1],[0, 0, -1, 1, 1, 1]] #상하좌우, 왼쪽위, 왼쪽아래 // 상하좌우, 오른쪽위, 오른쪽아래

# 외부에 노출되지 않은 빈칸에 대해 count를 세지 않기 위해 빈칸을 기준으로 bfs 진행
def bfs(y,x):
    q = deque()
    q.append((y,x))
    visited = [[0]*(W+2) for _ in range(H+2)]
    visited[y][x] = 1

    count = 0

    while q:
        py, px = q.popleft()
        for i in range(6):
            ny, nx = py+dy[i], px+dx[py%2][i]

            if 0<=ny<H+2 and 0<=nx<W+2 and not visited[ny][nx]:
                if arr[ny][nx]==0:
                    visited[ny][nx] = 1
                    q.append((ny,nx))
                else:
                    count+=1

    return count

print(bfs(0,0))