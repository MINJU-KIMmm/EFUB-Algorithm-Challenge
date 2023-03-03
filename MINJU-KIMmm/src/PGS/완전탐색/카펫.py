def solution(brown, yellow):
    def valid(ga, se):
        if ga<se:
            return False
        if yellow==(ga-2)*(se-2) and brown==(ga*se)-yellow:
            return True
        return False
    
    answer = []
    total = brown+yellow
    
    for i in range(1, total+1):
        if total%i != 0:
            continue
        j = total//i
        
        if valid(i, j):
            return [i, j]
    
    return answer
