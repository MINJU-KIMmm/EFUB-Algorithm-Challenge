import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().strip().split()))

stack = [(0, arr[0])]
answer = [0]
for i in range(1, N):
    now = arr[i]
    while stack and stack[-1][1] < now:
        stack.pop()

    if stack:
        answer.append(stack[-1][0]+1)
    else:
        answer.append(0)

    stack.append((i, arr[i]))

print(*answer)
