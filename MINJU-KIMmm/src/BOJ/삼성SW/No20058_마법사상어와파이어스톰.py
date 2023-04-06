import copy
from collections import deque
N, Q = map(int, input().split())
A = [list(map(int, input().strip().split())) for _ in range(2**N)]
L = list(map(int, input().strip().split()))

#temp_A = copy.deepcopy(A)

def rotate(l):
    global new_arr, A
    new_arr = [[0 for _ in range(2**N)] for _ in range(2**N)]

    box_size = 2**l
    half_size = 2**(l-1)

    for i in range(0, 2**N, 2**l):
        for j in range(0, 2**N, 2**l):
            move(i, j, half_size, 0)
            move(i, j+half_size,half_size, 1)
            move(i+half_size, j, half_size, 2)
            move(i+half_size, j+half_size, half_size, 3)
    A = copy.deepcopy(new_arr)

dir_x = [0, 1, -1, 0]
dir_y = [1, 0, 0, -1]
def move(start_row, start_col, half_size, move_dir):
    global new_arr
    for row in range(start_row, start_row+half_size):
        for col in range(start_col, start_col+half_size):
            nx = row+dir_x[move_dir]*half_size
            ny = col+dir_y[move_dir]*half_size

            new_arr[nx][ny] = A[row][col]

ddx = [-1, 1, 0, 0]
ddy = [0, 0, -1, 1]
def melt():
    melt_list = []
    for i in range(2**N):
        for j in range(2**N):
            if A[i][j] != 0:
                count = 0
                for dd in range(4):
                    nx, ny = i+ddx[dd], j+ddy[dd]
                    if 0<=nx<2**N and 0<=ny<2**N:
                        if A[nx][ny] != 0:
                            count += 1
                if count < 3:
                    melt_list.append((i,j))

    for i, j in melt_list:
        A[i][j] -= 1

answer2 = 0
answer1 = 0
def bfs(x,y):
    global answer1, answer2

    q = deque()
    visited[x][y] = 1
    q.append((x,y))
    cnt = 1
    answer1 += A[x][y]

    while q:
        px, py = q.popleft()

        for i in range(4):
            nx, ny = px+ddx[i], py+ddy[i]
            if 0<=nx<size and 0<=ny<size and not visited[nx][ny]:
                if A[nx][ny] != 0:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
                    cnt += 1
                    answer1 += A[nx][ny]

    return cnt

size = 2**N
visited = [[0] * size for _ in range(size)]
new_arr = [[0]*(2**N) for _ in range(2**N)]
#print(L)
for q in range(Q):
    # 회전하기
    rotate_board = [[0]*(2**N) for _ in range(2**N)]

    relate = [[[0]*2 for _ in range(2**L[q])] for _ in range(2**L[q])]

    for i in range(0, 2**L[q]):
        for j in range(0, 2**L[q]):
            new_i = j
            new_j = 2**L[q]-i-1

            relate[i][j][0] = new_i - i
            relate[i][j][1] = new_j - j

    for i in range(0, 2**N, 2**L[q]):
        for j in range(0, 2**N, 2**L[q]):
            for ii in range(i, i+2**L[q]):
                for jj in range(j, j+2**L[q]):
                    rotate_board[ii+relate[ii-i][jj-j][0]][jj+relate[ii-i][jj-j][1]] = A[ii][jj]

    A = copy.deepcopy(rotate_board)
    melt()

for i in range(size):
    for j in range(size):
        if not visited[i][j] and A[i][j]!=0:
            answer2 = max(bfs(i, j), answer2)


print(answer1)
print(answer2)