N, kim, lim = map(int, input().split())
count = 0

while kim!=lim:
    kim -= kim//2
    lim -= lim//2
    count+=1

print(count)

# 토너먼트의 규칙을 찾아야 함
# 다른 플레이어들은 계산 X, 2명의 인덱스만 알아내면 됨

# 8 -> 4 -> 2 -> 1 -> 1
# 9 -> 5 -> 3 -> 2 -> 1