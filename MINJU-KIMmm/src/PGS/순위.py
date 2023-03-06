from collections import deque

def solution(n, results):
    answer = 0
    
    win_lose = [['n']*(n) for _ in range(n)]
    for w, l in results:
        win_lose[w-1][l-1] = True
        win_lose[l-1][w-1] = False
        
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if win_lose[j][i] == 'n':
                    continue
                if win_lose[j][i] == win_lose[i][k]:
                    win_lose[j][k] = win_lose[j][i]
                    win_lose[k][j] = not win_lose[j][i]
    
    print(win_lose)
    for i in range(n):
        if 'n' in win_lose[i][:i] + win_lose[i][i+1:]:
            continue
        answer += 1
        
    return answer
