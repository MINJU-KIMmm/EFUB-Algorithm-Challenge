A, B = input().split()


min_count = len(B)+1

for i in range(len(B)-len(A)+1):
    count = 0
    for j in range(len(A)):
        if B[i+j]!=A[j]:
            count+=1
            if count>min_count:
                break
    if min_count>count:
        min_count = count
    if min_count == 0:
        break


print(min_count)


