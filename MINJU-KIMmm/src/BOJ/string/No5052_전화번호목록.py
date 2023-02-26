import sys, heapq

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    flag = True

    arr = [input().strip() for _ in range(n)]
    arr.sort()

    print(arr)

    for i in range(n-1):
        if arr[i] == arr[i+1][:len(arr[i])]:
            flag = False
            break

    if flag:
        print("YES")
    else:
        print("NO")



