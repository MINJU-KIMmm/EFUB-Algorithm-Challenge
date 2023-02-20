import math

#실버 5
# 에라토스테네스의 체
N = int(input())
arr = list(map(int, input().split()))
arr.sort()

prime = [False, False] + [True]*(arr[-1]-1)

for i in range(2, int(math.sqrt(arr[-1]))+1):
    if prime[i]:
        j = 2
        while i*j < len(prime):
            prime[i*j] = False
            j += 1

count = 0
for num in arr:
    if prime[num]:
        count += 1

print(count)