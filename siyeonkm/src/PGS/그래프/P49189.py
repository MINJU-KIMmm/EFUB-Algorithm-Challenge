from queue import Queue


def longestDest(n, edges):
    que = Queue()

    #방문여부 체크용 + 해당 노드까지의 최단거리 저장용
    #시작하는 노드인 1번은 최단거리가 0으로 저장될거기 때문에 -1로 초기화
    visited = [-1 for i in range(n + 1)]

    que.put((1, 0))
    visited[1] = 0

    while que.qsize() > 0:
        before = que.get()
        befNode = before[0]
        befLength = before[1]

        for node in edges[befNode]:
            #양방향 edge이므로 재방문 가능성이 있으므로 반드시 visited 체크 필요
            if visited[node] == -1:
                que.put((node, befLength + 1))
                print({"next": node, "length": befLength+1})
                print("")
                visited[node] = befLength + 1

    m = max(visited)
    answer = 0
    for length in visited:
        if length == m:
            answer += 1
    return answer


def solution(n, edge):
    answer = 0
    edges = [[] for i in range(n + 1)]

    for e in edge:
        edges[e[0]].append(e[1])
        edges[e[1]].append(e[0])

    answer = longestDest(n, edges)

    return answer


if __name__ == '__main__':
    edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    print(edge)
    output = solution(6, edge)
    print(output)