"""
1.전형적인 미로에서 최단거리찾기 알고리즘
2.1칸1칸이니까 가중치는 없으므로 bfs로 풀 수 있음
3.시작위치,도착위치도 포함해야함
4.입력되는 미로값이 서로 다 붙어서 한 수로 입력된다는점 잊지말기
5.최단거리는 어차피 여러번 방문돼야하므로 넣을때는 check하지만 뽑을때는 안함

"""
from collections import deque
import sys
input = sys.stdin.readline


def bfs(n, m, maze):
    deq = deque()
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    deq.append((0, 0))

    while deq:
        now = deq.popleft()
        y = now[0]
        x = now[1]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m and maze[ny][nx] == 1:
                deq.append((ny, nx))
                maze[ny][nx] = maze[y][x] + 1

    return maze[n-1][m-1]


if __name__ == '__main__':
    n, m = map(int, input().split())
    maze = [[] for _ in range(n)]

    for i in range(n):
        line = input().strip()
        for j in range(m):
            maze[i].append(int(line[j]))

    output = bfs(n, m, maze)
    print(output)
