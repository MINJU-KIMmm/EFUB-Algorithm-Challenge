from collections import deque

def bfs(n, computers, root, visited):
    visited[root] = 1
    q = deque()
    q.append(root)
    
    while q:
        now = q.popleft()
        
        for next in range(n):
            if computers[now][next] and not visited[next]:
                q.append(next)
                visited[next] = 1
    

def solution(n, computers):
    
    answer = 0
    
    visited = [0 for _ in range(n)]
    
    for i in range(n):
        if not visited[i]:
            bfs(n, computers, i, visited)
            answer += 1
                
    return answer

