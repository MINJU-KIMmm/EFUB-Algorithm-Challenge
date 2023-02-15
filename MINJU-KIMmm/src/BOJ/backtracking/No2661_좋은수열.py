N = int(input())

answer = ''


def dfs(idx, num):
    global answer

    # 절반 길이 만큼 검사한다.
    for i in range(1, (idx//2)+1):
        if num[-i:] == num[-2*i:-i]:
            return -1

    if idx == N:
        answer = num
        return 0

    for i in range(1, 4):
        if dfs(idx+1, num+str(i)) == 0:
            return 0


def solution():
    global answer
    dfs(0, '')
    return answer

print(solution())