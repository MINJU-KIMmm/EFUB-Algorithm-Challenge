S = int(input())

index = 0
sum = 0
for i in range(1, S + 1):
    sum+=i
    if sum>=S:
        index=i
        break

if S==sum:
    print(index)
else:
    print(index-1)