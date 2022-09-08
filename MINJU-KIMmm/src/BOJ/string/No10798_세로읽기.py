arr = [input() for _ in range(5)]
maxL = 0

for s in arr:
    maxL = max(len(s), maxL)

for j in range(maxL):
    for i in range(5):
        if j>=len(arr[i]):
            continue
        else:
            print(arr[i][j], end="")
        