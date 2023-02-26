"""
일반적인 그래프 탐색이므로 bfs든 dfs든 상관없으나, 서서히 퍼지는거니까 bfs로 풀고싶음
주어지는 노드들은 다 같은 그래프가 아니고, 그래프가 여러개일수도, 아예 연결안됐을수도 있음
걸리는건 무조건 1번부터. 근데 테케보니까 1번은 걸린수에 포함 안되는듯
"""

import sys
from collections import deque
input = sys.stdin.readline


def solution(n, graph):
    answer = -1
    visited = {}
    que = deque()
    que.append(1)

    while que:
        now = que.popleft()
        if now not in visited:
            visited[now] = True
            answer += 1

            for node in graph[now]:
                if node not in visited:
                    que.append(node)

    return answer


if __name__ == '__main__':
    n = int(input())
    e = int(input())
    graph = {}

    for i in range(e):
        v1, v2 = map(int, input().split())
        if v1 not in graph:
            graph[v1] = list()
        if v2 not in graph:
            graph[v2] = list()
        graph[v1].append(v2)
        graph[v2].append(v1)

    if 1 not in graph:
        print("0")
    else:
        output = solution(n, graph)
        print(output)
