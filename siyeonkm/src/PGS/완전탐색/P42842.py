def calculate(brown, x, y):
    if x * 2 + y * 2 + 4 == brown:
        return True
    else:
        return False


def solution(brown, yellow):
    answer = []
    max = yellow + 1
    if yellow > 1:
        max = yellow // 2 + 1

    for i in range(1, max):
        x = yellow // i
        y = i

        if yellow % i == 0 and x >= y:
            print({"x": x, "y": y})
            result = calculate(brown, x, y)
            if result == True:
                answer = [x + 2, y + 2]
    return answer