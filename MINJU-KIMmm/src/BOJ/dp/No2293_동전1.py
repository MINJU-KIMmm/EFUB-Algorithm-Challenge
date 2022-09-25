n, k = map(int, input().split())

arr = [int(input()) for _ in range(n)]

dp = [0 for _ in range(k+1)]
dp[0]=1

for c in arr:
    for i in range(c, k+1):
        dp[i]+=dp[i-c]

print(dp[k])