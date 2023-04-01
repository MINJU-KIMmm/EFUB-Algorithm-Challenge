import sys
from collections import deque

input = sys.stdin.readline
S = input().strip()
T = input().strip()


def bfs():
    q = deque()
    visited = set()
    visited.add(T)
    q.append(T)

    while q:
        now = q.popleft()
        if now == S:
            return 1
        if now!='' and now[-1]=='A':
            new_str = now[:-1]
            if new_str not in visited:
                q.append(new_str)
                visited.add(new_str)
        if now!='' and now[0]=='B':
            new_str = now[::-1][:-1]
            if new_str not in visited:
                q.append(new_str)
                visited.add(new_str)

    return 0


print(bfs())
