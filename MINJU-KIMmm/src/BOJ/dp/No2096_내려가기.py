import sys, copy

input = sys.stdin.readline
N = int(input())

a, b, c = map(int, input().strip().split())

max_dp = [a,b,c]
min_dp = [a,b,c]

for i in range(1, N):
    a, b, c = map(int, input().strip().split())

    mx1 = max(max_dp[0], max_dp[1])+a
    mx2 = max(max_dp[0], max_dp[1], max_dp[2])+b
    mx3 = max(max_dp[1], max_dp[2])+c

    max_dp = [mx1, mx2, mx3]

    mn1 = min(min_dp[0], min_dp[1])+a
    mn2 = min(min_dp[0], min_dp[1], min_dp[2])+b
    mn3 = min(min_dp[1], min_dp[2])+c

    min_dp = [mn1, mn2, mn3]

print(max(max_dp), min(min_dp))