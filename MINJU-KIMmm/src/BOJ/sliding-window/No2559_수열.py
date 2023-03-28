import sys

input = sys.stdin.readline
N, K = map(int, input().split())
arr = list(map(int, input().strip().split()))
max_val = sum(arr[:K])

before = max_val
for i in range(1, N-K+1):
    temp = before-arr[i-1]+arr[i+K-1]
    max_val = max(max_val, temp)
    before = temp

print(max_val)