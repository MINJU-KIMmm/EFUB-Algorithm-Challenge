import sys

input = sys.stdin.readline

N = int(input())
D = [list(map(int, input().strip().split())) for _ in range(N)]

dp = [[1e9 for _ in range(1<<N)] for _ in range(20)]

def recur(cnt, visit):
    # 모든 사람한테 분배 완료
    if visit == (1<<N)-1:
        return 0

    # 메모제이션 해둔 거 있으면 꺼내 씀
    if dp[cnt][visit] != 1e9:
        return dp[cnt][visit]

    for i in range(N):
        bit = 1<<i

        # 이미 일 배분(방문)
        if visit&bit:
            continue

        dp[cnt][visit] = min(recur(cnt+1, visit|bit) + D[cnt][i], dp[cnt][visit])

    return dp[cnt][visit]

print(recur(0, 0))