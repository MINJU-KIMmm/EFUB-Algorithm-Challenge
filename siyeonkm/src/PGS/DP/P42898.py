def findPath(m, n, puddles):
    dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
    dp[1][1] = 1

    for y in range(1, n + 1):
        for x in range(1, m + 1):
            if [x, y] in puddles or [x, y] == [1, 1]:
                continue
            else:
                dp[y][x] += dp[y - 1][x] + dp[y][x - 1]
                dp[y][x] %= 1000000007

    return dp[n][m]


def solution(m, n, puddles):
    answer = 0
    answer = findPath(m, n, puddles)
    return answer


if __name__ == '__main__':
    puddles = [[2, 1], [2, 2], [2, 3], [4, 2], [4, 3], [4, 4], [6, 2], [6, 3]]
    print(puddles)
    output = solution(7, 4, puddles)
    print(output)
