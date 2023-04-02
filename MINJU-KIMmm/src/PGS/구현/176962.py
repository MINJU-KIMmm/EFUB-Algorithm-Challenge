# 시간 계산
def calc_time(time):
    hour = int(time[:2])
    minute = int(time[3:])
    
    return hour*60+minute

def solution(plans):
    answer = []
    plans.sort(key=lambda x:x[1])
    stop = [] # 스택 - 멈춘 할일들 저장
    
    for i, (name, time, play) in enumerate(plans[:-1]):
        time = calc_time(time)
        next_time = calc_time(plans[i+1][1])
        play = int(play)
        this_time = next_time - time #다음 할일까지 남은 시간
        # 시간 딱 맞춰서 이번 할 일 완료
        if this_time-play == 0:
            answer.append(name)
        # 할일 남음 - stop
        elif this_time-play < 0:
            play -= this_time
            stop.append((play, name))
        # 할일 다 했는데 시간 남은 경우
        else:
            answer.append(name)
            this_time -= play
            # 멈췄던 할 일들 순서대로 할 수 있는만큼 한다.
            while stop and this_time:
                stop_time, stop_name = stop.pop()
                if this_time-stop_time == 0:
                    answer.append(stop_name)
                    this_time -= stop_time
                    break
                elif this_time-stop_time < 0:
                    stop_time -= this_time
                    stop.append((stop_time, stop_name))
                    this_time -= stop_time
                    break
                else:
                    answer.append(stop_name)
                    this_time -= stop_time
    
    answer.append(plans[-1][0]) # 마지막 할일
    # 마지막 할일 끝나고도 멈춰있었던 할일들이 있다면 순서대로 추가
    while stop:
        answer.append(stop.pop()[1])
    return answer
