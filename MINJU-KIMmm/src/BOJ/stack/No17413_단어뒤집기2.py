S = input()
stack = []


for i in range(len(S)):

    if S[i]=='>':
        stack.append(S[i])

        while stack:
            print(stack.pop(0), end="")

    elif S[i]=='<':
        while stack:
            print(stack.pop(), end="")
        stack.append(S[i])

    elif S[i] == ' ':
        if stack[0]=='<':
            stack.append(S[i])
        else:
            while stack:
                print(stack.pop(), end="")
            print(" ", end="")

    else:
        stack.append(S[i])

while stack:
    print(stack.pop(), end="")