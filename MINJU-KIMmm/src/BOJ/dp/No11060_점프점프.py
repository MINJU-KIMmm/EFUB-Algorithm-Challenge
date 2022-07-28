N = int(input())
arr = list(map(int, input().split()))

dp=[N+1]*N
dp[0]=0

for i in range(N):
    for j in range(1, arr[i]+1):
        if i+j<N:
            dp[i+j]=min(dp[i+j], dp[i]+1)

if dp[N-1]==N+1:
    print(-1)
else:
    print(dp[N-1])