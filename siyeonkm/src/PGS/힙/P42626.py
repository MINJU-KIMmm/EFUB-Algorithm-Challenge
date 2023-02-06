import heapq


def mix(scoville):
    min_1 = heapq.heappop(scoville)
    min_2 = heapq.heappop(scoville)
    heapq.heappush(scoville, min_1 + min_2 * 2)


def solution(scoville, K):
    answer = 0

    # 당연히 파라미터로 처음에 받은 scoville은 heap형태로 정렬된게 아님
    # 그러니까 heapify로 정렬을 해준다음에 min을 뽑아야함
    heapq.heapify(scoville)
    min = scoville[0]

    if min >= K:
        return answer

    while min < K and len(scoville) >= 2:
        mix(scoville)
        min = scoville[0]
        answer += 1

    if min < K:
        return -1
    else:
        return answer