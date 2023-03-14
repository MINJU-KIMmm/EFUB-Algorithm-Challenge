import sys

input = sys.stdin.readline
N = int(input())

arr = [[0]*2 for _ in range(N+1)]

for i in range(N):
    T, P = map(int, input().split())
    arr[i+1][0] = T
    arr[i+1][1] = P

end_dp = [0 for _ in range(N+2)]
max_val = 0
for i in range(1, N+1):
    end_dp[i] = max(end_dp[i], end_dp[i-1])
    if arr[i][0]+i <= N+1:
        profit = end_dp[i]+arr[i][1]
        end_dp[arr[i][0]+i] = max(end_dp[arr[i][0]+i], profit)

#print(end_dp)
print(max(end_dp))