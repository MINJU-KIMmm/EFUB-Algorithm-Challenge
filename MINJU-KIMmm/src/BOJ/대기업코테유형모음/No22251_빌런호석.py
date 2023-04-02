import sys

input = sys.stdin.readline
N, K, P, X = map(int, input().split())

dic2 = {0:"1110111", 1:"0010010", 2:"0111101", 3:"0111011", 4:"1011010", 5:"1101011", 6:"1101111", 7:"0110010", 8:"1111111", 9:"1111011"}

actual = '0'*(K-len(str(X))) + str(X)

def compare(start, target):
    s_light = dic2[int(start)]
    t_light = dic2[int(target)]

    count = 0
    for l in range(len(s_light)):
        if s_light[l] != t_light[l]:
            count += 1
    return count

def canChange(target):
    start = list(actual)
    target = list('0'*(K-len(str(target)))+str(target))

    change = 0
    for i in range(K):
        change += compare(start[i], target[i])
    if change>P:
        return False
    else:
        return True

total = 0
for i in range(1, N+1):
    if i==X:
        continue
    if canChange(i):
        total += 1

print(total)