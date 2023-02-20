import math

# 에라토스테네스의 체
M, N = map(int, input().split())

flag = [False, False] + [True]*(N-1)

for i in range(2, int(math.sqrt(N))+1):
    if flag[i]:
        j = 2
        while i*j < len(flag):
            flag[i*j] = False
            j += 1

for i in range(M, N+1):
    if flag[i]:
        print(i)