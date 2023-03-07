import sys

input = sys.stdin.readline
N, M = map(int, input().split())

A = list(map(int, input().split()))

start, end = 0, 0
sum = A[0]
count = 0
while start<len(A) and end<len(A):
    if sum==M:
        count += 1
        sum -= A[start]
        start += 1
    elif sum>M:
        sum -= A[start]
        start += 1
    else:
        end += 1
        if end>=N:
            break
        sum += A[end]

print(count)