N = int(input())
M = int(input())
S = input()
total = 2*N+1

answer = 0
count = 0
i = 1

while i<M-1:
    if S[i-1]=='I' and S[i]=='O' and S[i+1]=='I':
        count += 1
        if count==N:
            answer+=1
            count-=1
        i+=1
    else:
        count = 0

    i+=1

print(answer)