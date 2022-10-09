import sys

N = int(input())
arr = sorted(list(map(int, input().split())))

left = 0
right = N-1

standard = sys.maxsize
answer_list = []
while left<right:
    total = arr[left]+arr[right]

    # 0과 가까운 값 standard 담기 : 비교되는 기준 값
    if abs(total) < standard:
        standard = abs(total)
        answer_list = [arr[left], arr[right]]

    if total < 0:
        left += 1
    else:
        right -= 1

print(answer_list[0], answer_list[1])