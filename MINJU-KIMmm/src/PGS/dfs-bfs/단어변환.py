from collections import deque
import sys

def solution(begin, target, words):
    q = deque()
    q.append((begin, 0)) #현재 단어, 바꾼 횟수
    visited = [0 for _ in range(len(words))]
    answer = sys.maxsize
    
    if target not in words:
        return 0
    
    while q:
        w, cnt = q.popleft()
        if w==target:
            answer = min(cnt, answer)
        
        for i in range(len(words)):
            count = 0

            for j in range(len(w)):
                if w[j]!=words[i][j]:
                    count+=1
                    
            if count==1 and not visited[i]:
                q.append((words[i], cnt+1))
                visited[i] = 1
    
    return answer

    
                    
