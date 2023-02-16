def search(phone_dict, num):
    l = phone_dict[num]
    l.sort()

    for i in range(len(l)-1):
        for j in range(len(l[i])):
            if l[i][j] != l[i+1][j]:
                return False
        return True
    return False


def solution(phone_book):
    answer = True
    phone_dict = {}

    for phone in phone_book:
        first = phone[0]
        l = phone_dict.get(first, [])
        l.append(phone)
        phone_dict[first] = l

    for i in range(1, 10):
        if str(i) in phone_dict:
            if search(phone_dict, str(i)):
                answer = False
                break

    return answer

if __name__ == '__main__':
    data = ["12", "1", "234", "245"]
    output = solution(data)
    print(output)
