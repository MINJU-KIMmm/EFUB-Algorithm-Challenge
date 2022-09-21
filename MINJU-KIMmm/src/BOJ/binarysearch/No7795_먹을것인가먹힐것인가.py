import bisect

T = int(input())

while T:
    N, M = map(int, input().split())
    count = 0

    A = list(map(int,input().split()))
    B = sorted(list(map(int,input().split())))

    for i in range(len(A)):
        left = 0
        right = len(B)-1
        answer = -1

        while left<=right:

            mid = (left+right)//2

            if A[i]<=B[mid]:
                right = mid-1
            else:
                left = mid+1
                answer = mid

        count += answer+1

    print(count)


    T-=1

###############################################################

#라이브러리 이용
for _ in range(int(input())):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = sorted(list(map(int, input().split())))

    count = 0
    for a in A:
        count+=(bisect.bisect_left(B, a))
    print(count)