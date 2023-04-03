import sys

input = sys.stdin.readline
n = int(input())

stack = []
answer = 0

for _ in range(n):
    x, y = map(int, input().split())

    if y!=0:
        while stack:
            # 같은 높이면 더하지 x
            if stack[-1]==y:
                break
            # 크면 더하고 스택에도 추가
            elif stack[-1] < y:
                stack.append(y)
                answer += 1
                break
            # 작으면 pop 시켜서 같거나 크거나 스택이 빌때까지 pop
            else:
                stack.pop()
        # 스택이 비었으면 y추가 후 +1
        if not stack:
            stack.append(y)
            answer += 1
    # 0 나오면 새로 시작
    else:
        stack = []

print(answer)