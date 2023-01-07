# 뭔가 dfs로 풀면서 ㅈ되는거 같다는 생각이 들었는데, 최단거리는 bfs로 풀어야한다고함
# 아무래도...dfs는 한길만 파는데, 그럼 미로에서 헤맬 수 있음
# 반대로 bfs는 가까운순으로 탐색하니까 최단거리 계산가능
# 다만, 각 좌표마다 몇번만에 도달했는지 갱신해주는 배열이 필요할듯

from queue import Queue


def bfs(n, m, maps):
    visited = [[False for i in range(m)] for j in range(n)]
    que = Queue()
    que.put((0, 0, 1))
    visited[0][0] = True

    while que.qsize() > 0:
        x, y, length = que.get()

        if x == n - 1 and y == m - 1:
            return length

        if x - 1 >= 0 and maps[x - 1][y] == 1 and visited[x - 1][y] == False:
            que.put((x - 1, y, length + 1))
            # 큐에 집어넣을때 미리 visited =true로 해놓기
            # 꺼낼때 true로 하면, 큐에 이미 가기로하고 넣어놨음에도 불구하고 누군가가 꺼내기 전에 방문하려한다면 방문이 가능하기 때문
            # 그러면 효율성면에서 떨어짐
            visited[x - 1][y] = True
        if x + 1 < n and maps[x + 1][y] == 1 and visited[x + 1][y] == False:
            que.put((x + 1, y, length + 1))
            visited[x + 1][y] = True
        if y - 1 >= 0 and maps[x][y - 1] == 1 and visited[x][y - 1] == False:
            que.put((x, y - 1, length + 1))
            visited[x][y - 1] = True
        if y + 1 < m and maps[x][y + 1] == 1 and visited[x][y + 1] == False:
            que.put((x, y + 1, length + 1))
            visited[x][y + 1] = True

    return -1


def solution(maps):
    answer = bfs(len(maps), len(maps[0]), maps)
    return answer


if __name__ == '__main__':
    maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]
    answer = solution(maps)
    print(answer)
