dx = [-1, 1, 0, 0, -1, -1, 1, 1] #T, B, L, R, LT, RT, LB, RB
dy = [0, 0, -1, 1, -1, 1, -1, 1]

move_dic = {'T':0, 'B':1, 'L':2, 'R':3, 'LT':4, 'RT':5, 'LB':6, 'RB':7}

K, R, N = input().split()
N = int(N)

kx = 8-int(K[1])
ky = ord(K[0])-ord('A')

rx = 8-int(R[1])
ry = ord(R[0])-ord('A')

for i in range(N):
    move = input()
    d = move_dic.get(move)
    nx, ny = kx+dx[d], ky+dy[d]

    if 0<=nx<8 and 0<=ny<8:
        if nx==rx and ny==ry:
            nrx, nry = rx+dx[d], ry+dy[d]
            if 0<=nrx<8 and 0<=nry<8:
                rx, ry = nrx, nry
                kx, ky = nx, ny
        else:
            kx, ky = nx, ny

k_loc = (chr(ky+ord('A'))) + str(8-kx)
r_loc = (chr(ry+ord('A'))) + str(8-rx)
print(k_loc)
print(r_loc)
