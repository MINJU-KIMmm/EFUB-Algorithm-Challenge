N = int(input())
first = list(input())

for _ in range(N-1):
    diff = list(input())
    for i in range(len(diff)):
        if first[i]!=diff[i]:
            first[i] = '?'

print("".join(first))