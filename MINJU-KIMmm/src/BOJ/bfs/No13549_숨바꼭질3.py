from collections import deque

N, K = map(int, input().split())

q = deque()
q.append(N)

visited = [-1 for _ in range(100001)]
visited[N]=0

def bfs():
    while q:
        cur = q.popleft()
        if cur == K:
            return visited[cur]

        # 0초 뒤 순간 이동
        if 0 < cur * 2 < 100001 and visited[cur * 2] == -1:
            q.appendleft(cur * 2)
            visited[cur * 2] = visited[cur]

        # 1초 뒤 X-1
        if 0 <= cur-1 < 100001 and visited[cur-1]==-1:
            q.append(cur-1)
            visited[cur-1] = visited[cur] + 1

        # 1초 뒤 X+1
        if 0 <= cur+1 < 100001 and visited[cur+1]==-1:
            q.append(cur+1)
            visited[cur+1] = visited[cur] + 1



print(bfs())