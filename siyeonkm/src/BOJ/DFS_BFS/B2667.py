"""
역시 탐색이니까 bfs dfs인데 상하좌우 탐색하는거니까 bfs로 하자
이번에는 길을 탐색하는게 아니고 그룹이 몇개인지 탐색하는거
처음 제출하니까 시간초과가 났음 어떻게 해결해야할까
"""

import sys
from collections import deque
input = sys.stdin.readline


def get_next(village, n):
    for i in range(n):
        for j in range(n):
            if village[i][j] == 1:
                return (i, j)
    return (n, n)


def solution(n, village):
    flag = True
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    count_list = []

    while flag:
        count = 0
        que = deque()

        curr = get_next(village, n)
        if curr == (n, n):
            flag = False
            break
        else:
            que.append(curr)

        while que:
            now = que.popleft()
            y = now[0]
            x = now[1]

            if village[y][x] == 1:
                village[y][x] = 0
                count += 1

                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if 0 <= ny < n and 0 <= nx < n and village[ny][nx] == 1:
                        que.append((ny, nx))
        count_list.append(count)
    return count_list


if __name__ == '__main__':
    n = int(input())
    village = [[] for _ in range(n)]

    for i in range(n):
        line = input().strip()
        for j in range(n):
            village[i].append(int(line[j]))

    output = solution(n, village)
    output.sort()
    print(len(output))
    for i in range(len(output)):
        print(output[i])