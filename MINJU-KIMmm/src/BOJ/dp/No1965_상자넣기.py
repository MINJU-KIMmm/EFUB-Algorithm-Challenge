n = int(input())
arr = list(map(int, input().split()))

dp = [0]*(max(arr)+1)

for i in range(n):
    num = arr[i]
    before = max(dp[:num])
    dp[num] = max(dp[num], before+1) #같은 크기 상자가 여러 번 나올 수 있기 때문에 최대값으로 구해줘야 함

print(max(dp))

