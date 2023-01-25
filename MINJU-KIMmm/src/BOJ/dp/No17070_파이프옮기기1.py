N = int(input())

#<dp>
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)] # type, 행, 열

for i in range(1, N):
    if arr[0][i] == 0:
        dp[0][0][i] = 1
    else:
        break

for i in range(1, N):
    for j in range(1, N):
        #대각선
        if arr[i][j] == 0 and arr[i-1][j] == 0 and arr[i][j-1] == 0:
            dp[2][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]
        #가로 세로
        if arr[i][j] == 0:
            dp[0][i][j] = dp[0][i][j-1]+dp[2][i][j-1]
            dp[1][i][j] = dp[1][i-1][j]+dp[2][i-1][j]

print(sum(dp[i][N-1][N-1] for i in range(3)))
# <dfs>
#
# cnt = 0
#
# t0 = 0
# t1 = 1
# t2 = 2
#
# def dfs(x, y, type):
#     global cnt
#     if x==N-1 and y==N-1:
#         cnt += 1
#         return
#
#     #대각선
#     if x+1 < N and y+1 < N and arr[x+1][y+1] == 0 and arr[x][y+1] == 0 and arr[x+1][y] == 0:
#         dfs(x+1, y+1, t2)
#     #가로
#     if type == t0 or type == t2:
#         if y+1 < N and arr[x][y+1] == 0:
#             dfs(x, y+1, t0)
#     #세로
#     if type == t1 or type == t2:
#         if x+1 < N and arr[x+1][y] == 0:
#             dfs(x+1, y, t1)
#
#
# dfs(0, 1, t0)
# print(cnt)