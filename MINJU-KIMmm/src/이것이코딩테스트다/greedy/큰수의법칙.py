N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)

one = arr[0]
two = arr[1]

sum = 0
while(True):
    for _ in range(K):
        if M==0:
            break
        sum+=one
        M-=1
    if M==0:
        break
    sum+=two
    M-=1

print(sum)
