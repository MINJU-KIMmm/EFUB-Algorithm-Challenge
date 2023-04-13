import sys
from collections import deque

input = sys.stdin.readline
S = input().strip()
T = input().strip()

visited = set()
def bfs():
    q = deque()
    q.append(T)
    visited.add(T)

    while q:
        now = q.popleft()
        if now == S:
            return 1
        if now == '':
            return 0

        if now[-1]=='A':
            next_ = now[:-1]
            if next_ not in visited:
                visited.add(next_)
                q.append(next_)
        if now[0]=='B':
            next_ = now[1:][::-1]
            if next_ not in visited:
                visited.add(next_)
                q.append(next_)

    return 0

print(bfs())