str = input()

left = 0
right = len(str)-1

while left<=right:
    if str[left]!=str[right]:
        print(0)
        exit()

    left+=1
    right-=1

print(1)