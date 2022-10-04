N, M = map(int, input().split())
S = [input() for _ in range(N)]

count = 0
for _ in range(M):
    string = input()
    if string in S:
        count += 1

print(count)