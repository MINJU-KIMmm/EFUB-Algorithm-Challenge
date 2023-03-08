import sys

input = sys.stdin.readline

N,M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

#그냥 정렬
#
# add = []
#
#
# add = (A+B)
# add.sort()
# print(*add)

# 투포인터
l, r = 0, 0
add = []
while l<N and r<M:
    if A[l]<B[r]:
        add.append(A[l])
        l += 1
    else:
        add.append(B[r])
        r += 1

# 길이가 안 맞는 경우 원소 남음
while l<N:
    add.append(A[l])
    l += 1
while r<M:
    add.append(B[r])
    r += 1

print(*add)