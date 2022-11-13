N = int(input())

arr = [int(input()) for _ in range(N)]
arr.sort()

size = len(arr)
max_val = 0

for i in range(len(arr)):
    use = size-i #중량 들기에 참여할 줄 개수(자기랑 자기보다 큰애들이 참여해야 최대중량)
    max_val = max(use*arr[i], max_val) # 최대값 구하기

print(max_val)