import sys
from collections import deque

input = sys.stdin.readline


def dfs(v, graph, visit):
    if not visit[v]:
        visit[v] = True
        print(v, end=" ")
        for node in graph[v]:
            if not visit[node]:
                dfs(node, graph, visit)
    else:
        return


def bfs(v, graph, visit):
    queue = deque()
    queue.append(v)

    while queue:
        now = queue.popleft()
        if not visit[now]:
            print(now, end=" ")
            visit[now] = True
        else:
            continue

        for node in graph[now]:
            if not visit[node]:
                queue.append(node)


def solution(n, v, graph):
    visit = [False for _ in range(n + 1)]
    dfs(v, graph, visit)
    print()
    visit = [False for _ in range(n + 1)]
    bfs(v, graph, visit)


if __name__ == '__main__':
    n, e, v = map(int, input().split())
    graph = {}

    for i in range(e):
        v1, v2 = map(int, input().split())
        if v1 not in graph:
            graph[v1] = list()
        if v2 not in graph:
            graph[v2] = list()
        graph[v1].append(v2)
        graph[v2].append(v1)

    for key in graph:
        graph[key].sort()

    solution(n, v, graph)