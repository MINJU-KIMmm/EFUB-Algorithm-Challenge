n = int(input())

result = 0

arr = [[0]*101 for _ in range(101)]

for _ in range(n):
    a, b = map(int, input().split())
    for i in range(10):
        for j in range(10):
            arr[a+i][b+j] = 1


for i in arr:
    result+=sum(i)

print(result)