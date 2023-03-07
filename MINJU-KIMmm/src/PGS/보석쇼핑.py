# 투포인터
def solution(gems):
    N = len(gems)
    answer = [1, N]
    count = len(set(gems))
    
    gems = [0]+gems
    
    dic = {gems[1]:1}
    
    start, end = 1, 1 # 포인터 초기화. start & end = 처음 위치
    
    while start < N+1 and end < N+1:
        # 모든 종류 채운 경우
        if len(dic)==count:
            # answer에 있는 값보다 길이가 짧으면 갱신
            if end-start < answer[1]-answer[0]:
                answer = [start, end]
            
            # start +1 해서 다음 구간 찾음
            if dic[gems[start]] == 1:
                del dic[gems[start]]
            else:
                dic[gems[start]] -= 1
            
            start += 1
        # 종류 채우지 못한 경우
        else:
            # end + 1해서 범위 늘려서 찾음
            end += 1
            if end > N:
                break
            # dic.get(p1, p2) -> p1이 없으면 p2로 초기화 
            dic[gems[end]] = dic.get(gems[end], 0) + 1
    
    return answer
