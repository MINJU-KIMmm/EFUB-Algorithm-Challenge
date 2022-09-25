from collections import deque

arr = [list(input()) for _ in range(12)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(x, y):
    q = deque([(x,y)])
    visited[x][y]=True
    list = []
    list.append((x,y))

    while q:
        px, py = q.popleft()

        for i in range(4):
            nx, ny = px+dx[i], py+dy[i]

            if 0<=nx<12 and 0<=ny<6 and not visited[nx][ny]:
                if arr[x][y]==arr[nx][ny]:
                    visited[nx][ny]=True
                    q.append((nx,ny))
                    list.append((nx,ny))

    return list


#뿌요 아래에 빈칸이 있으면 내려가도록
def down():
    for i in range(6):
        for j in range(10,-1,-1):
            for k in range(11, j, -1):
                if arr[j][i]!='.' and arr[k][i]=='.':
                    arr[k][i]=arr[j][i]
                    arr[j][i]='.'
                    break

answer = 0
while True:
    play = False
    visited = [[False]*6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if arr[i][j]!='.' and not visited[i][j]:
                list = bfs(i,j)
                if len(list)>=4:
                    play = True
                    for x, y in list:
                        arr[x][y]='.'
    if not play:
        break
    down()
    answer+=1


print(answer)
