from collections import deque

N,M = map(int, input().split())

arr = [0 for _ in range(101)]

#사다리
for _ in range(N):
    x, y = map(int, input().split())
    arr[x] = y

#뱀
for _ in range(M):
    u, v = map(int, input().split())
    arr[u] = -1*v

visited = [0 for _ in range(101)]


def bfs():
    q = deque()
    q.append(1)
    visited[1] = 1

    while q:
        pos = q.popleft()
        if pos == 100:
            return
        for i in range(1,7):
            npos = pos+i
            if 1<=npos<=100 and not visited[npos]:
                if arr[npos]>0: #사다리
                    visited[npos] = visited[pos] + 1
                    npos = arr[npos]
                elif arr[npos]<0: #뱀
                    visited[npos] = visited[pos] + 1
                    npos = arr[npos]*(-1) #다시 -1곱해서 양수로 만들어 줌

                if not visited[npos]:
                    q.append(npos)
                    visited[npos] = visited[pos] + 1

bfs()
print(visited[100]-1)
