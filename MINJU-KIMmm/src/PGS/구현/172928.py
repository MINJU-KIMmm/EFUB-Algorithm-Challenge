def solution(park, routes):
    answer = []
    
    dir = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}
    
    # 시작점과 공원 정보 기록
    arr = [['O']*len(park[0]) for _ in range(len(park))]
    x,y = 0, 0
    for i, p in enumerate(park):
        for j in range(len(p)):
            if p[j]=='S':
                x, y = i, j
            if p[j]=='X':
                arr[i][j] = 'X'
                
    for r in routes:
        d, n = r.split(' ')
        n = int(n)
        
        px, py = x, y
        flag = True
        for i in range(n):
            nx, ny = px+dir[d][0], py+dir[d][1]
            if 0<=nx<len(park) and 0<=ny<len(park[0]) and arr[nx][ny]!='X':
                px, py = nx, ny
            else:
                flag = False
                break
        # 끝까지 이동할 수 있었을 경우에만 이동
        if flag:
            x, y = px, py
        
    return [x, y]
