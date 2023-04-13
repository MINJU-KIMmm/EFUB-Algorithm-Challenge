from collections import deque

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
# -1 : 검은 돌 / 0 : 빨강 / 1~m : 빨강 아닌 폭탄
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 1
visited = [[0] * n for _ in range(n)]  # 빨강은 여러개 그룹에 속할 수도 있다 -> 방문처리 x


def bfs(x, y):
    group = []
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    color = arr[x][y]
    group.append((x, y))

    red = []
    while q:
        px, py = q.popleft()

        for i in range(4):
            nx, ny = px + dx[i], py + dy[i]

            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != -1 and not visited[nx][ny]:
                if arr[nx][ny] == color or arr[nx][ny]==0:
                    q.append((nx, ny))
                    group.append((nx, ny))
                    visited[nx][ny] = 1
                    if arr[nx][ny]==0:
                        red.append((nx,ny))

    for x, y in red:
        visited[x][y] = 0

    return group


# 빨강 개수
def red_size(group):
    size = 0
    for x, y in group:
        if arr[x][y] == 0:
            size += 1
    return size


# 기준점 찾기
def mark(group):
    group.sort(key=lambda x: (-x[0], x[1]))
    for x, y in group:
        if arr[x][y] != 0:
            return x, y


def pick():
    min_red = 20 * 20
    reds = []
    num = 0
    for i in range(len(group_info)):
        group = group_info[i]
        if min_red == red_size(group):
            reds.append((i, group))
        elif min_red > red_size(group):
            reds = []
            reds.append((i, group))
            num = i

    if len(reds) == 1:
        return num
    else:
        marks = []
        for i in range(len(reds)):
            group = reds[i][1]
            marks.append((i, mark(group)))
        marks.sort(key=lambda x: (-x[0], x[1]))
        return marks[0][0]


# 폭탄제거
def remove_bomb(num):
    group = group_info[num]
    # h_change = [0 for _ in range(n)]
    for x, y in group:
        arr[x][y] = -2
        # h_change[y] += 1


def down():
    for col in range(n):
        for row in range(n - 2, -1, -1):
            # 화산이 있으면
            if arr[row][col] != -2 and arr[row][col] != -1:
                next_row = row + 1
                while True:
                    # 바닥이거나 뭔가 있으면 그만
                    if next_row >= n or (next_row < n and arr[next_row][col] != -2):
                        next_row -= 1
                        break
                    next_row += 1

                # print(row, col, next_row)
                color = arr[row][col]
                arr[row][col] = -2
                arr[next_row][col] = color


def rotate():
    temp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[n - 1 - j][i] = arr[i][j]

    for i in range(n):
        for j in range(n):
            arr[i][j] = temp[i][j]


score = 0
while True:
    visited = [[0] * n for _ in range(n)]
    group_info = []
    max_size = 2
    for i in range(n):
        for j in range(n):
            if arr[i][j] >= 1 and not visited[i][j]:
                this_group = bfs(i, j)
                if max_size == len(this_group):
                    group_info.append(this_group)
                elif max_size < len(this_group):
                    group_info = []
                    group_info.append(this_group)
                    max_size = len(this_group)

    if not group_info:
        break

    pick_num = 0
    if len(group_info) > 1:
        pick_num = pick()

    # print(pick_num)
    remove_bomb(pick_num)
    down()
    rotate()
    down()

    score += max_size * max_size

    # for a in arr:
    #     print(*a)

    # 폭탄 묶음이 없는 경우

    ############ 지워야 됨
    # break

print(score)