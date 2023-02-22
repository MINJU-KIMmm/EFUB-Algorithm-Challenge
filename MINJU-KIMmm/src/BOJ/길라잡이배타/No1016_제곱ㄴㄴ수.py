import sys, math

input = sys.stdin.readline
min_, max_ = map(int, input().strip().split())

nono = [True]*(max_-min_+1)

i = 2
answer = len(nono)
while i < int(math.sqrt(max_))+1:
    temp = i*i
    # Remain : 소수점 보정 (제곱수가 딱 나누어 떨어지면 상관 없지만 그게 아니라면 소수점이 버림 처리됨)
    remain = 0 if min_%temp==0 else 1
    j = min_//temp + remain
    while temp*j <= max_:
        if nono[temp*j-min_]:
            nono[temp*j-min_] = False
            answer -= 1
        j+=1
    i += 1

print(answer)