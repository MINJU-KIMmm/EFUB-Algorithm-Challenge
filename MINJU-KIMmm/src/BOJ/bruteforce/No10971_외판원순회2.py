import sys

N = int(input())

W = [list(map(int, input().split())) for _ in range(N)]
answer = sys.maxsize


def dfs(start, next, value, visited):
    global answer

    #전체 다 방문했으면 최소값 갱신 & 시작점으로 다시 돌아오는 값 더해줌
    if len(visited)==N:
        if W[next][start]!=0:
            answer = min(answer, value+W[next][start])
        return

    for i in range(N):
        # 방문 취소할 조건 필요(백트래킹)
        # 현재의 가장 작은 값(answer)보다 value값이 크거나 같으면 무시해야 함 -> 아니면 시간 초과!!
        if W[next][i]!=0 and i not in visited and value<answer:
            visited.append(i)
            dfs(start, i, value+W[next][i], visited)
            visited.pop()


#모든 출발지에 대해서 dfs방문
for i in range(N):
    dfs(i,i,W[i][i],[i])


print(answer)
