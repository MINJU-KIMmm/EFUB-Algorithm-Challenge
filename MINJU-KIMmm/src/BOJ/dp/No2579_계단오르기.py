n = int(input())
arr = list(int(input()) for _ in range(n))
arr.insert(0, 0)

dp = [0]*(n+1)
dp[1] = arr[1]

# 범위체크 필요!
if n>1:
    dp[2] = arr[1]+arr[2]
if n>2:
    dp[3] = max(arr[1]+arr[3], arr[2]+arr[3])

for i in range(4, n+1):
    dp[i] = max(arr[i-1]+dp[i-3], dp[i-2]) + arr[i]

print(dp[n])