from collections import deque

F, S, G, U, D = map(int, input().split())


def bfs():
    while q:
        cur = q.popleft()
        if cur == G:
            return move[cur]
        # up
        up = cur+U
        if up<=F and not visited[up]:
            q.append(up)
            move[up]=move[cur]+1
            visited[up]=True

        #down
        down = cur-D
        if down>=1 and not visited[down]:
            q.append(down)
            move[down]=move[cur]+1
            visited[down]=True

    if move[G]==0:
        return "use the stairs"


visited = [False for _ in range(F+1)]
move = [0 for _ in range(F+1)]

q = deque([S])
visited[S] = True

cnt = bfs()
print(cnt)