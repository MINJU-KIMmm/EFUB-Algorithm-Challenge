import sys

input = sys.stdin.readline

n, k = map(int, input().split())
dp = [sys.maxsize for _ in range(k+1)]

arr = [int(input()) for _ in range(n)]
arr.sort()

dp[k] = 0
for i in range(k, -1, -1):
    for j in arr:
        if i-j>=0:
            dp[i-j] = min(dp[i-j], dp[i]+1)
        else:
            break

#print(dp)
if dp[0]==sys.maxsize:
    print(-1)
else:
    print(dp[0])