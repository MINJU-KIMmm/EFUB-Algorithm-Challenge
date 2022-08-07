import copy

H, W = map(int, input().split())

arr = list(map(int, input().split()))
left = copy.deepcopy(arr)
right = copy.deepcopy(arr)

for i in range(1, len(arr)):
    left[i]=max(left[i], left[i-1])

for i in range(len(right)-2, -1, -1):
    right[i]=max(right[i], right[i+1])

sum=0
for i in range(W):
    sum+=(min(right[i], left[i])-arr[i])

print(sum)