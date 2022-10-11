def dfs(numbers, target, index, sum):
    if len(numbers) == index:
        return 1 if sum == target else 0
    else:
        return dfs(numbers, target, index + 1, sum + numbers[index]) + dfs(numbers, target, index + 1,
                                                                           sum - numbers[index])


def solution(numbers, target):
    answer = 0
    answer = dfs(numbers, target, 0, 0)
    return answer