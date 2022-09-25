
N, M = map(int, input().split())

arr = list(map(int, input().split()))

# 블루레이 크기
left = 0
right = sum(arr)

answer = right
while left<=right:
    mid = (left+right)//2

    # 이거 없으면 틀림
    if mid<max(arr):
        left = mid+1
        continue

    cnt = 0
    temp = 0
    for i in range(len(arr)):
        if temp+arr[i]<=mid:
            temp+=arr[i]
        else:
            temp = arr[i]
            cnt+=1

    cnt+=1 #마지막 남은 애들 그룹


    if cnt<=M: # 크기가 너무 크다
        right = mid-1
        answer = min(answer, mid)
    elif cnt>M:
        left = mid+1


print(answer)