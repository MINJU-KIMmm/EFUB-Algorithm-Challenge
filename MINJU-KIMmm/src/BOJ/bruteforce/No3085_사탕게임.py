from collections import deque
import copy
N = int(input())
arr = [list(map(str, input())) for _ in range(N)]

dx = [1,0]
dy = [0,1]


def candy_count():
    answer = 1

    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if arr[i][j]==arr[i][j-1]:
                cnt+=1
            else:
                cnt = 1

            if cnt>answer:
                answer = cnt
        cnt = 1
        for j in range(1, N):
            if arr[j][i] == arr[j - 1][i]:
                # 이전 것과 같다면 cnt에 1 더하기
                cnt += 1
            else:
                # 이전과 다르다면 다시 1로 초기화
                cnt = 1

            # 비교해서 현재 cnt가 더 크다면 answer 갱신하기
            if cnt > answer:
                answer = cnt

    return answer


max_count = 0
temp = copy.deepcopy(arr)
for i in range(N):
    for j in range(N):
        if j+1 < N:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]

            temp_max = candy_count()
            if temp_max>max_count:
                max_count = temp_max

            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]

        if i + 1 < N:
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]

            temp_max = candy_count()
            if temp_max > max_count:
                max_count = temp_max

            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]

print(max_count)



