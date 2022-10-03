before = list(input())
given = list(input())

stack = []

for i in range(len(before)):
    stack.append(before[i])
    #스택의 가장 위가 폭발문자열의 끝자리와 같고 스택의 길이가 폭발문자열의 길이 이상인 경우 -> 이 때만 비교하여 모든 순간에 비교하지 않도록 할 수 있다
    if stack[-1]==given[-1] and len(stack)>=len(given):
        #위의 조건을 만족한다면 폭탄 문자열이 스택에 포함되었는지 확인하고 pop하여 제거
        if stack[-len(given):]==given:
            for _ in range(len(given)):
                stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")


