S = input()
for c in S:
    if c.islower():
        print(chr(97+(ord(c)+13-97)%26), end="")
    elif c.isupper():
        print(chr(65+(ord(c)+13-65)%26), end="")
    else:
        print(c, end="")