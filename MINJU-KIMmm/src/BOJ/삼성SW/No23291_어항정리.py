import copy

# ㅁㅜㄹ고기 수가 가장 적은 어항에 물고기 한마리 넣기
def put_min():
    min_val = 10**8
    min_list = []
    for i in range(N):
        for j in range(len(arr[i])):
            if min_val > arr[i][j]:
                min_list = []
                min_list.append((i,j))
                min_val = arr[i][j]
            elif min_val ==arr[i][j]:
                min_list.append((i,j))
    for x, y in min_list:
        arr[x][y] += 1

# 처음 왼쪽에 있는 어항 위에 쌓기
def init_left():
    elem = arr[0].pop(0)
    arr[1].append(elem)

# 어항 쌓기
def up():
    # 열
    len_list = []
    height = [0 for _ in range(N)] # 각 열의 높이
    for a in arr:
        len_list.append(len(a))

    for i in range(len(len_list)):
        for j in range(len_list[i]):
            height[j] += 1

    #print(two)
    temp = [[] for _ in range(height[0])]
    for i in range(N):
        if height[i]>=2:
            for h in range(height[i]):
                temp[h].append(arr[h][i])
    #print(temp)
    turn = [[0]*len(temp) for _ in range(len(temp[0]))]
    if len(turn[0])>len(arr[0])-len(turn):
        return False

    for i in range(len(temp)):
        for j in range(len(temp[0])):
            turn[j][len(temp)-1-i] = temp[i][j]
            #turn[len(temp[0])-1-j][i] = temp[i][j]

    #print('turn', turn)
    #print(arr)
    for i in range(len(height)):
        if height[i]>=2:
            for row in range(N):
                if arr[row]:
                    arr[row].pop(0)
    #print(arr)
    idx = 1
    for i in range(len(turn)-1, -1, -1):
        for j in range(len(turn[0])-1, -1, -1):
            arr[idx].append(turn[i][j])
        idx += 1

    return True

def fish_size():
    temp = [[0 for _ in range(N)] for _ in range(N)]

    row = 0
    dc = [-1, 1]
    while row < N and arr[row]:
        for col in range(len(arr[row])):
            for ddc in range(2):
                nc1 = col+dc[ddc]
                if 0<=nc1<len(arr[row]):
                    #print(nc1, len(arr[row]))
                    diff = abs(arr[row][col] - arr[row][nc1])//5
                    if arr[row][col] < arr[row][nc1]:
                        temp[row][col] += diff
                    else:
                        temp[row][col] -= diff
        row += 1

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            for ddc in range(2):
                nr1 = i+dc[ddc]
                if 0<=nr1<N and j<len(arr[nr1]):
                    diff = abs(arr[i][j]-arr[nr1][j])//5
                    if arr[i][j] < arr[nr1][j]:
                        temp[i][j] += diff
                    else:
                        temp[i][j] -= diff

    for i in range(N):
        for j in range(N):
            if temp[i][j]:
                arr[i][j] += temp[i][j]

def make_line():
    temp = [[]*N for _ in range(N)]
    row = 0
    col = 0

    idx = 0
    for c in range(len(arr[0])):
        for r in range(N):
            if c>=len(arr[r]):
                break
            #print(r, c)
            temp[0].append(arr[r][c])
            #idx += 1

    return temp

def half_up(h):
    half = len(arr[0])//2

    turn = [[0 for _ in range(half)] for _ in range(h)]

    for i in range(h):
        for j in range(half):
            turn[h-1-i][half-1-j] = arr[i][j]
    #print('a', arr)
    for i in range(h):
        for j in range(half):
            arr[i].pop(0)

    #print('a', arr)
    for i in range(h):
        for j in range(half):
            arr[h+i].append(turn[i][j])

def max_min():
    min_val = 10001
    max_val = 0
    for i in range(len(arr)):
        if not arr[i]:
            break
        min_val = min(arr[i])
        max_val = max(arr[i])

    return max_val - min_val



N, K = map(int, input().split())

#MAX  = 101
arr = [[]*N for _ in range(N)]
inputs = list(map(int, input().split()))
for i in range(N):
    arr[0].append(inputs[i])

answer = 0

while max_min()>K:
    answer += 1
    put_min()
    init_left()
    while True:
        if not up():
            break

    fish_size()
    arr = copy.deepcopy(make_line())
    half_up(1)
    #print(arr)
    half_up(2)
    fish_size()
    arr = copy.deepcopy(make_line())
    #print(arr)


print(answer)