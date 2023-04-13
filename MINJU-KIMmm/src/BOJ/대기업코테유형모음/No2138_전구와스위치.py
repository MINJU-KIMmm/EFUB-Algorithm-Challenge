import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
#arr = [list(input().strip()) for _ in range(N)]
light = list(map(int, input().strip()))
goal = list(map(int, input().strip()))

answer = 0

def change(A, B):
    L = A[:]
    press = 0

    for i in range(1, N):
        # 이전 전구가 같은 상태면 패스
        if L[i-1]==B[i-1]:
            continue
        # 상태 다름
        press += 1
        for j in range(i-1, i+2):
            if j<N:
                L[j] = 1-L[j]
    return press if L==B else 1e9

# 첫번째 전구의 스위치 누르지 않은 경우
res = change(light, goal)
# 누른 경우
light[0] = 1-light[0]
light[1] = 1-light[1]

res = min(res, change(light, goal)+1)
print(res if res != 1e9 else -1)