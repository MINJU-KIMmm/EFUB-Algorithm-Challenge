def dfs(start, depth):
    if depth == 6:
        for i in range(6):
            print(comb[i], end=' ')
        print()
        return

    for i in range(start, len(s)):
        comb.append(s[i])
        dfs(i+1, depth+1)
        comb.pop()

while True:
    s = list(map(int, input().split()))

    comb = []
    if s[0] == 0:
        break

    dfs(1,0)
    print()