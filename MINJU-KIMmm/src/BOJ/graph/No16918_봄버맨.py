from collections import deque

R, C, N = map(int, input().split())
arr = [list(input()) for _ in range(R)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def save_location():
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 'O':
                bomb_list.append((i,j))

def full():
    for i in range(R):
        for j in range(C):
            if arr[i][j] == '.':
                arr[i][j] = 'O'

def bomb():
    while bomb_list:
        x, y = bomb_list.popleft()
        arr[x][y] = '.'

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<R and 0<=ny<C and arr[nx][ny]=='O':
                arr[nx][ny] = '.'


N-=1
while N:
    bomb_list = deque()

    save_location()

    full()
    N-=1
    if N==0:
        break

    bomb()
    N-=1

for i in arr:
    print("".join(i))