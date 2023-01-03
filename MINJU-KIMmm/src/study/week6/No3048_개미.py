N1, N2 = map(int, input().split())
group1 = list(input())
group2 = list(input())

arr = []
for i in group1[::-1]:
    arr.append((i,0))
for i in group2:
    arr.append((i,1))

T = int(input())

while T:
    T -= 1
    index = []
    for i in range(len(arr)-1):
        if arr[i][1]==0 and arr[i+1][1]==1:
            index.append(i)
    for i in index:
        arr[i], arr[i+1] = arr[i+1], arr[i]
for i, j in arr:
    print(i, end='')