N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]

left = min(arr)
right = sum(arr)

while left<=right:
    mid = (left+right)//2 #인출 금액
    count = 1 #인출 횟수
    money = mid #지금 가진 돈

    for i in range(N):
        if money<arr[i]:
            #인출
            money = mid
            count += 1
        money -= arr[i] #돈 씀

    if count>M or mid<max(arr):
        left = mid+1
    else:
        right = mid-1
        k = mid

print(k)