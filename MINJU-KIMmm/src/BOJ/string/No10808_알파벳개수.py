S = input()
count = [0 for _ in range(26)]

for c in S:
    count[ord(c)-97]+=1

for i in count:
    print(i, end=" ")