N = int(input())
info = [list(map(int, input().split())) for _ in range(N**2)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

pos = [[0]*N for _ in range(N)] # 좌석 배열

for order in range(N**2):
    students = info[order]
    tmp = []

    for i in range(N):
        for j in range(N):
            if pos[i][j]==0: # 빈자리 라면
                like = 0
                blank = 0
                for k in range(4):
                    nx, ny = i+dx[k], j+dy[k]
                    if 0<=nx<N and 0<=ny<N:
                        if pos[nx][ny] in students[1:]: #인접 학생이 좋아하는 학생인지
                            like+=1
                        if pos[nx][ny]==0: #인접 자리가 빈자린지
                            blank+=1
                tmp.append([like, blank, i, j])

    tmp.sort(key=lambda x:(-x[0], -x[1], x[2], x[3])) #람다 이용해서 조건에 맞게 우선순위 정렬
    pos[tmp[0][2]][tmp[0][3]] = students[0] #정렬 후 가장 앞에 있는 값의 위치 정보에 해당 학생 삽입

result = 0
info.sort() #인덱스로 학생 누군지 판별 위해 정렬

for i in range(N):
    for j in range(N):
        ans = 0
        for k in range(4):
            nx, ny = i+dx[k], j+dy[k]
            if 0<=nx<N and 0<=ny<N:
                if pos[nx][ny] in info[pos[i][j]-1]:
                    ans+=1

        if ans!=0:
            result+=10**(ans-1)


print(result)