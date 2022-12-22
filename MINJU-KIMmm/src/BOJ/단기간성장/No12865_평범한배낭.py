N, K = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
dp = [[-1]*(K+1) for _ in range(N)] #dp[살펴본 물건 idx][남은 담을 수 있는 무게]

def bag(i, k):
    if i<0:
        return 0

    if dp[i][k]==-1:
        if k<arr[i][0]:
            dp[i][k] = bag(i-1, k)
        else:
            dp[i][k] = max(bag(i-1,k), bag(i-1,k-arr[i][0])+arr[i][1])

    return dp[i][k]

print(bag(N-1, K))