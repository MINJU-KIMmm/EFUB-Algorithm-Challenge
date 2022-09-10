T = int(input())

while T:
    arr = input().split()

    for s in arr:
        for i in range(len(s)-1,-1,-1):
            print(s[i],end='')
        print(" ", end='')

    print()

    T-=1