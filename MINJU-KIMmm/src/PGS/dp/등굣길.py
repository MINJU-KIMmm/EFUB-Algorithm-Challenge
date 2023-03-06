def solution(m, n, puddles):
    answer = 0
    
    dp = [[0]*m for _ in range(n)]
    
    for i, j in puddles:
        dp[j-1][i-1] = 'X'
            
    for i in range(m):
        if dp[0][i]=='X':
            break
        dp[0][i] = 1
    for i in range(n):
        if dp[i][0] == 'X':
            break
        dp[i][0] = 1
        
                        
    for i in range(1, n):
        for j in range(1, m):
            if dp[i][j] != 'X':
                if dp[i-1][j] != 'X' and dp[i][j-1] != 'X':
                    dp[i][j] = (dp[i-1][j]+dp[i][j-1])%1000000007
                elif dp[i-1][j] == 'X' and dp[i][j-1] != 'X':
                    dp[i][j] = (dp[i][j-1])
                else:
                    dp[i][j] = dp[i-1][j]
    answer = (dp[n-1][m-1])%1000000007
    return answer
