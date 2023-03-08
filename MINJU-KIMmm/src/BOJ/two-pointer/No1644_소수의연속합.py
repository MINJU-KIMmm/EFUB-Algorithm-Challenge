import math

n = int(input())
prime = []
arr = [False, False] + [True]*(n-1)

for i in range(2, int(math.sqrt(n))+1):
    if arr[i]:
        j = 2
        while i*j <= n:
            arr[i*j] = False
            j+=1

for i in range(2, n+1):
    if arr[i]:
        prime.append(i)

count = 0
end = 0
start = 0
sum_ = 0

while True:
    if sum_ == n:
        count += 1
    if sum_ > n:
        sum_ -= prime[start]
        start += 1
    elif end == len(prime):
        break
    else:
        sum_ += prime[end]
        end += 1

# count = 0
# end = 0
# start = 0
#
# while 0 <= start <= end <= len(prime):
#     sum_ = sum(prime[start:end])
#     if sum_ == n:
#         count += 1
#         end += 1
#     elif sum_ < n:
#         end += 1
#     else:
#         start += 1

print(count)