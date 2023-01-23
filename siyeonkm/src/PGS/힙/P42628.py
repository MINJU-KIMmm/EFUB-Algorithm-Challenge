import heapq


def deleteMax(heap_q):
    heap_max = []
    heap_min = []
    for item in heap_q:
        heapq.heappush(heap_max, -item)
    heapq.heappop(heap_max)
    for item in heap_max:
        heapq.heappush(heap_min, -item)
    return heap_min


def deleteMin(answer):
    #왜인지는 잘 모르겠으나 list안에 값이 1개만 있는 경우에는 list가 아니라 그냥 변수가 되어버림
    #그래서 자꾸 heap함수에는 list를 넣어야한다는 오류가 생기길래 .extend를 사용함
    heap_q = []
    heap_q.extend(answer)

    heapq.heappop(heap_q)
    return heap_q

def addNum(num, answer):
    heap_q = []
    heap_q.extend(answer)

    heapq.heappush(heap_q, num)
    return heap_q


def solution(operations):
    answer = []

    for operation in operations:
        if "I" in operation:
            num = int(operation[2:])
            answer = addNum(num, answer)

        elif len(answer) != 0:
            if "-" in operation:
                answer = deleteMin(answer)
            else:
                answer = deleteMax(answer)
        print({"operation":operation, "heap":answer})
        print("")

    if len(answer) == 0:
        return [0, 0]
    else:
        minNum = heapq.nsmallest(1, answer)[-1]
        maxNum = heapq.nlargest(1, answer)[-1]
        return [maxNum, minNum]


if __name__ == '__main__':
    l = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
    output = solution(l)
    print({"answer": output})
