# diffs = 퍼즐 난이도 순서 1차원 정수배열   ->  for diff in diffs:
# 현재 퍼즐의 난이도를 diff
# diff ≤ level  ->  time_cur  / level - diff >= 0  ->  time_cur
# diff > level이면, 퍼즐을 총 diff - level번 틀립니다.  
# level - diff < 0  ->  ( time_cur + time_prev ) * (diff - level) + time_cur
# times = 퍼즐 소요시간 순서 1차원 정수 배열
# 현재 퍼즐의 소요 시간을 time_cur
# 이전 퍼즐의 소요 시간을 time_prev
# times[idx]로 idx 설정해서 현재와 이전 구분
# limit = 전체 제한 시간   limit - 소요시간
# 당신의 숙련도를 level
# 제한 시간 내에 성공하는 숙련도의 최솟값(정수)
def solution(diffs, times, limit):
    level = 0
    suc_time = limit + 1
    while suc_time > limit :
        suc_time = 0
        level += 1  
        for idx, diff in enumerate(diffs): 
            if level - diff < 0 :  # 난이도가 높을 때 
                suc_time += ( times[idx] + times[idx-1] ) * (diff - level) + times[idx] 
                
            else  : # 숙련도가 높거나 같을때
                suc_time += times[idx]
            
            if suc_time > limit : 
                break
                
    return left
