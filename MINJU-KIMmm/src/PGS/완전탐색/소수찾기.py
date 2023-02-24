import math


nums = []
def solution(numbers):
    answer = 0
    
    
    for i in range(1, len(numbers)+1):
        dfs(i, '', list(numbers), [0]*len(numbers))
    
    max_val = max(nums)
    flag = check(max_val)
    
    result = set(nums)
    for num in result:
        if flag[num]:
            answer += 1
    
    return answer

def dfs(leng, num, numbers, visited):
    if leng == len(num):
        nums.append(int(num))
        return
    
    for i in range(len(numbers)):
        if not visited[i]:
            # if len(num) == 0 and numbers[i]=='0' and leng!=1:
            #     continue
                
            visited[i] = 1
            dfs(leng, num+numbers[i], numbers, visited)
            visited[i] = 0

        

def check(num):
    flag = [False, False] + [True]*(num-1)
    
    for i in range(2, int(math.sqrt(num))):
        if flag[i]:
            j = 2
            while i*j<len(flag):
                flag[i*j] = False
                j += 1
    
    return flag
    
