import sys


def check(num, data):
    answer = 1

    for i in range(num):
        count = 1
        for j in range(1, num):
            if data[i][j] == data[i][j - 1]:
                count += 1
                if count > answer:
                    answer = count
            else:
                count = 1


        count = 1
        for j in range(1, num):
            if data[j][i] == data[j - 1][i]:
                count += 1
                if count > answer:
                    answer = count
            else:
                count = 1

    return answer


def solution(num, data):
    answer = 0

    for i in range(num):
        for j in range(num):
            if j + 1 < num:
                data[i][j], data[i][j + 1] = data[i][j + 1], data[i][j]
                longest = check(num, data)

                if longest > answer:
                    answer = longest

                data[i][j], data[i][j + 1] = data[i][j + 1], data[i][j]

            if i + 1 < num:
                data[i][j], data[i + 1][j] = data[i + 1][j], data[i][j]
                longest = check(num, data)

                if longest > answer:
                    answer = longest

                data[i][j], data[i + 1][j] = data[i + 1][j], data[i][j]

    return answer


if __name__ == '__main__':
    inputs = sys.stdin.readline
    num = int(inputs())
    data = [list(inputs().rstrip()) for _ in range(num)]
    output = solution(num, data)
    print(output)
