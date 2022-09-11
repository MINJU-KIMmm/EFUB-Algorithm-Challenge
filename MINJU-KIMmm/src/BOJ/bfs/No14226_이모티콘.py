from collections import deque

S = int(input())

q = deque()
visited = [[-1] * (S+1) for _ in range(S+1)]
visited[0][1] = 0 #초기 상태(클립보드는 비어있고, 화면에는 1개)
q.append((0, 1))  # 클립보드, 화면


def bfs():
    while q:
        x, y = q.popleft()

        # 1번. 화면에 있는 이모티콘을 모두 복사하여 클립보드에 저장하는 경우
        cnt = y
        screen = y
        if visited[cnt][screen] == -1:
            visited[cnt][screen] = visited[x][y] + 1
            q.append((cnt, screen))

        # 2번. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 하는 경우
        cnt = x
        screen = y + x
        if screen<=S and visited[cnt][screen] == -1:
            visited[cnt][screen] = visited[x][y] + 1
            q.append((cnt, screen))

        # 3번. 화면에 있는 이모티콘 중 하나를 삭제하는 경우
        cnt = x
        screen = y - 1
        if screen>=0 and visited[cnt][screen] == -1:
            visited[cnt][screen] = visited[x][y] + 1
            q.append((cnt, screen))


bfs()
answer = 1e9
for i in range(S+1):
    if visited[i][S] != -1:
        answer = min(answer, visited[i][S])

print(answer)