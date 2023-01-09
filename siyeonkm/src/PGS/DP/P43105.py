def calculate(triangle):
    for x in range(len(triangle)):
        if x == 0:
            continue

        for y in range(len(triangle[x])):
            parent_left = 0
            parent_right = 0

            if y - 1 >= 0:
                parent_left = triangle[x - 1][y - 1]
            if y <= x - 1:
                parent_right = triangle[x - 1][y]

            triangle[x][y] += max(parent_left, parent_right)

    return max(triangle[len(triangle) - 1])


def solution(triangle):
    answer = calculate(triangle)
    return answer