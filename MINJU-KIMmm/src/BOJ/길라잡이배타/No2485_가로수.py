import sys


input = sys.stdin.readline

N = int(input())
arr = list(int(input()) for _ in range(N))

arr.sort()

def GCD(a, b):
    while b>0:
        a, b = b, a%b
    return a

dists = []
for i in range(0, N-1):
    dis = arr[i+1]-arr[i]
    dists.append(dis)

g = dists[0]
for i in range(1, len(dists)):
    g = GCD(g, dists[i])

result = 0
for dis in dists:
    result += dis//g-1

print(result)

