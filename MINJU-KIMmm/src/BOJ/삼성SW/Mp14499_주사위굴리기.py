import sys

input = sys.stdin.readline
N, M, x, y, K = map(int, input().split())

arr = []
for _ in range(N):
    temp = list(map(int, input().strip().split()))
    arr.append(temp)

move = list(map(int, input().strip().split()))

dice = [0, 0, 0, 0, 0, 0]
pos_x, pos_y = x, y
dx = [0, 0, -1, 1] # x, 동, 서, 북, 남
dy = [1, -1, 0, 0]


def turn(dir):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if dir == 1: #동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c

    elif dir == 2: #서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d

    elif dir == 3: #북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b

    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e
for i in range(len(move)):
    dir = move[i]
    nx, ny = pos_x+dx[dir-1], pos_y+dy[dir-1]
    if 0<=nx<N and 0<=ny<M:
        pos_x = nx
        pos_y = ny

        turn(dir)
        if arr[pos_x][pos_y] == 0:
            arr[pos_x][pos_y] = dice[-1]
        else:
            dice[-1] = arr[pos_x][pos_y]
            arr[pos_x][pos_y]=0

        print(dice[0])
