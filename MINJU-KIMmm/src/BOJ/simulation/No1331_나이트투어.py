arr = [[0]*6 for _ in range(6)]

count = 1
before_row = 0
before_col = 0

start_row = 0
start_col = 0

for i in range(36):
    idx = input()
    row = int(idx[1])-1
    col = ord(idx[0])-ord('A')

    if not arr[row][col]:
        arr[row][col] = count
    else:
        print("Invalid")
        exit()

    if count!=1:
        if not ((abs(before_row-row)==2 and abs(before_col-col)==1) or (abs(before_row-row)==1 and abs(before_col-col)==2)):
            print("Invalid")
            exit()
    else:
        start_row = row
        start_col = col

    before_row = row
    before_col = col

    count += 1

if not ((abs(before_row - start_row) == 2 and abs(before_col - start_col) == 1) or (
        abs(before_row - start_row) == 1 and abs(before_col - start_col) == 2)):
    print("Invalid")
    exit()

print("Valid")