answer = 0
count = 0
def solution(word):
    global answer
    
    order = []
    alp = ['A', 'E', 'I', 'O', 'U']
    
    def dfs(w):
        global answer, count
        count += 1
        if len(w)==5 and w!=word:
            return
        
        if w==word:
            answer = count-1
            return
        
        for i in range(5):
            dfs(w+alp[i])
      
    dfs('')
    
    return answer
