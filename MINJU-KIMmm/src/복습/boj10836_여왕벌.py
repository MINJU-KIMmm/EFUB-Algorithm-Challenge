import sys

input = sys.stdin.readline
M, N = map(int, input().split())
arr = [1 for _ in range(2*M-1)]

def calc_line(zero, one, two):
    idx = zero
    while one and idx<2*M-1:
        arr[idx]+=1
        idx += 1
        one -= 1
    while two and idx<2*M-1:
        arr[idx]+=2
        idx += 1
        two -= 1


for _ in range(N):
    z, o, t = map(int, input().split())
    calc_line(z, o, t)

#first = arr[:M][::-1]

for i in range(M):
    print(arr[M-1-i], end=' ')
    print(*arr[M:])

