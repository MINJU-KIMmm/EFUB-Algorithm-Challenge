def solution(s):
    answer = True
    stack = []
    idx = 1

    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        else:
            if len(stack) <= 0:
                answer = False
                break
            else:
                top = stack.pop()
                if top != '(':
                    answer = False
                    break

    if len(stack) > 0:
        answer = False
    return answer