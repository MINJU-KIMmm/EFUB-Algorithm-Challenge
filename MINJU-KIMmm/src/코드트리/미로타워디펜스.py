n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
center = n//2 # 플레이어 위치

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0] # 나선형 이동 방향(왼, 아, 오, 위) & 왼, 오 마다 길이 증가

mx = [0, -1, 0, 1]
my = [1, 0, -1, 0] # 몬스터 나선형 이동(오, 위, 왼, 아) & 왼, 오 마다 길이 감소

ax = [0, 1, 0, -1]
ay = [1, 0, -1, 0] # 공격 방향(오, 아, 왼, 위)

score = 0
# 나선형 번호 순서대로 담기
spiral = []
def make_spiral():
    cur_x, cur_y = center, center
    dir, num = 0, 1

    while cur_x or cur_y:
        for _ in range(num):
            cur_x += dx[dir]
            cur_y += dy[dir]

            spiral.append((cur_x, cur_y))

            if cur_x == 0 and cur_y == 0:
                break

        dir = (dir+1)%4
        if dir==0 or dir==2:
            num += 1


# 1. 공격
def attack(d, p):
    global score
    x, y = n//2, n//2
    for i in range(p):
        x += ax[d]
        y += ay[d]

        if 0<=x<n and 0<=y<n:
            score += arr[x][y]
            arr[x][y] = 0



temp = [[0 for _ in range(n)] for _ in range(n)]
# 2. 몬스터 이동
def mon_move():
    for i in range(n):
        for j in range(n):
            temp[i][j] = 0

    s_idx = 0
    for i, j in spiral:
        if arr[i][j]:
            tx, ty = spiral[s_idx]
            temp[tx][ty] = arr[i][j]
            s_idx += 1

    for i in range(n):
        for j in range(n):
            arr[i][j] = temp[i][j]


def find_end():
    for i, (x, y) in enumerate(spiral):
        if arr[x][y] == 0:
            return i-1

    return len(spiral)-1

# 3. 4번 이상 반복 시 삭제
def repeat(end):
    global score
    count = 0
    before = -1

    start_idx = 0
    same = -1
    flag = False
    start = []
    for i, (x, y) in enumerate(spiral[:end+1]):
        if before != arr[x][y]:
            count = 1
            start_idx = i
        else:
            count += 1

        if count == 4:
            start.append(start_idx)
            same = arr[x][y]
            flag = True

        before = arr[x][y]

    if flag:
        for ss in start:
            spiral_idx = ss
            x, y = spiral[spiral_idx]
            while spiral_idx<len(spiral) and arr[x][y] == same:
                score += same
                arr[x][y] = 0
                spiral_idx += 1
                if spiral_idx < len(spiral):
                    x, y = spiral[spiral_idx]

    return flag

def pair():
    pair_arr = []
    final_arr = []
    for x, y in spiral:
        if arr[x][y]!=0:
            pair_arr.append(arr[x][y])
            arr[x][y] = 0
    before = pair_arr[0]
    same_len = 1
    for i in range(1, len(pair_arr)):
        if before!=pair_arr[i]:
            final_arr.append(same_len)
            final_arr.append(before)
            same_len = 1
        else:
            same_len += 1
        before = pair_arr[i]

    if final_arr[-1]!=pair_arr[-1]:
        final_arr.append(1)
        final_arr.append(pair_arr[-1])


    for i, (sx, sy) in enumerate(spiral):
        if i<len(final_arr):
            arr[sx][sy] = final_arr[i]


make_spiral()
for _ in range(m):
    d, p = map(int, input().split())
    attack(d, p)

    mon_move()
    f = True

    while f:
        end = find_end()
        f = repeat(end)
        mon_move()

    pair()


print(score)
