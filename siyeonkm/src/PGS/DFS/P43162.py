# 제공된 배열에서 그래프가 몇개 나오는지 알아내는 문
def finishCheck(n):
    for i in range(n):
        if visit[i] == False:
            return i
    return n


def dfs(root, computers):
    global visit
    stack = []

    stack.append(root)
    while len(stack) > 0:
        now = stack.pop()
        visit[now] = True

        for i in range(len(computers[now])):
            if (computers[now][i] != 0 and i != now and not visit[i]):
                # 현재 node와 연결되어있고, 같은 node가 아니면서, 방문한적이 없다면 stack에 넣기
                stack.append(i)

    return


def solution(n, computers):
    answer = 0
    root = 0
    global visit
    visit = [False for i in range(n)]

    while True:
        root = finishCheck(n)
        if root != n:
            dfs(root, computers)
            answer += 1
        else:
            break

    return answer