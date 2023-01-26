N = int(input())
arr = []
empty = []
t = []
s = []

for i in range(N):
    inputs = list(input().split())
    for j in range(len(inputs)):
        if inputs[j]=='X':
            empty.append((i,j))
        if inputs[j]=='S':
            s.append((i,j))
        if inputs[j]=='T':
            t.append((i,j))
    arr.append(inputs)

visited = [0]*len(empty)


def check():

    for tx, ty in t:
        for x in range(tx, N):
            if arr[x][ty] == 'O':
                break
            if arr[x][ty] == 'S':
                return False
        for x in range(tx, -1, -1):
            if arr[x][ty] == 'O':
                break
            if arr[x][ty] == 'S':
                return False
        for y in range(ty, N):
            if arr[tx][y] == 'O':
                break
            if arr[tx][y] == 'S':
                return False
        for y in range(ty, -1, -1):
            if arr[tx][y] == 'O':
                break
            if arr[tx][y] == 'S':
                return False

    return True


def dfs(depth, start):
    if depth == 3:
        return check()

    for i in range(start, len(empty)):
        if not visited[i]:
            visited[i] = 1
            arr[empty[i][0]][empty[i][1]] = 'O'
            if dfs(depth+1, i+1):
                return True
            visited[i] = 0
            arr[empty[i][0]][empty[i][1]] = 'X'

if dfs(0, 0):
    print("YES")
else:
    print("NO")
