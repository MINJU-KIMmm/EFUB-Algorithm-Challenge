def bs(li, n):
    left = 0
    right = len(li)-1

    while left<=right:
        mid = (left+right)//2
        if li[mid]==n:
            return 1
        elif li[mid]<n:
            left = mid+1
        else:
            right = mid-1

    return 0



T = int(input())


for _ in range(T):

    N = int(input())
    note1 = sorted(list(map(int, input().split())))
    M = int(input())
    note2 = list(map(int, input().split()))

    for i in note2:
        print(bs(note1, i))

