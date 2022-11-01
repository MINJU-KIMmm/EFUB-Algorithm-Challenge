from itertools import combinations

while True:
    arr = list(map(int, input().split()))
    k = arr[0]
    if k == 0:
        break

    comb = combinations(arr[1:], 6)
    for i in comb:
        for j in range(6):
            print(i[j], end = ' ')
        print()
    print()