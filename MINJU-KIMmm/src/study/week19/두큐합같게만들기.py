def solution(queue1, queue2):
    answer = -1
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    q_sum = sum1 + sum2

    if q_sum % 2 != 0:
        return -1

    mid = q_sum // 2
    diff1 = mid - sum1
    diff2 = mid - sum2

    if abs(diff1) != abs(diff2):
        return -1

    idx1 = -1
    idx2 = -1

    part1 = 0
    part2 = 0

    while idx1 < len(queue1) and idx2 < len(queue2):
        if abs(part1 - part2) != abs(diff1):
            if part1 < part2:
                idx1 += 1
                if idx1 >= len(queue1):
                    break
                part1 += queue1[idx1]
            else:
                idx2 += 1
                if idx2 >= len(queue2):
                    break
                part2 += queue2[idx2]

        else:
            answer = (idx1+1) + (idx2+1)
            break

    return answer

print(solution([3, 2, 7, 2]	, [4, 6, 5, 1]))
print(solution([1, 2, 1, 2],	[1, 10, 1, 2]))
print(solution([1, 1],[1, 5]))