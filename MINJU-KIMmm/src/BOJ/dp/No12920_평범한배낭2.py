# 플래티넘 4
# dp, 비트마스킹
# 이중 반복문을 피하고 중복해서 더하는 경우(1+4 == 2+3)을 피하기 위해 비트마스킹을 사용
# 1+2+4 = 7 이런 식으로 2의 제곱수의 합만으로 모든 수를 표현할 수 있다는 것에서 부터 시작

N, M = map(int, input().split())

dp = [0 for _ in range(M+1)] #인덱스 : 남은 무게
info = [] #(weight, satisfact)

for _ in range(N):
    V, C, K = map(int, input().split())

    idx = 1
    while K>0:
        tmp = min(K, idx) #남은 개수를 초과하지 않는 선에서
        info.append((tmp*V, tmp*C)) #비트마스킹, 1, 2, 4, ... 배한 무게와 만족도를 담고 있는 배열을 만든다 (조합해서 더하면 모든 수의 배수 만들 수 있음)
        idx*=2
        K-=tmp

for v, c in info:
    for j in range(M, 0, -1):
        if j >= v:
            dp[j] = max(dp[j], dp[j-v]+c)

print(dp[M])