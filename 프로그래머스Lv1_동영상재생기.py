# prev = -10
# next = 10
# max = video_len
# 직전 재생위치 pos
# commands  사용자 입력이 들어가있음. 
# 결과는 op_end < pos < video_len

# 현재위치 pos <= op_end      ->  op_end
# 현재위치 pos >= video_len   ->  video_len
# pos < op_start             ->  pos
# op_end = op_start <= pos <= op_end

# ':'기준으로 나눔  -> split(':')
# map으로 나눈 요소들을  int로 만들어줌
#

# 초로 변경
def s_num(time_text):
    time_list = list(map(int, time_text.split(':')))

    mm = time_list[0]
    ss = time_list[1] + mm * 60
    return ss
    
def ms_text(ss):
    
    time_num_list = [ss//60, ss%60]
    time_list = list(map(str, time_num_list))
    
    return ':'.join([str(x).zfill(2) for x in time_list])

                    
def pos_point(len_n, pos_n, op_start_n, op_end_n):
    if pos_n < 0:
        pos_n = 0
    elif pos_n > len_n:
        pos_n = len_n
    elif op_start_n <= pos_n < op_end_n:
        pos_n = op_end_n
    return pos_n
    
    

def solution(video_len, pos, op_start, op_end, commands):
    
    video_len =s_num(video_len)
    pos=s_num(pos)
    op_start=s_num(op_start)
    op_end=s_num(op_end)
    
    for use in commands :
        pos = pos_point(video_len, pos, op_start, op_end)
        
        if use == 'prev' :
            pos -= 10
            pos = pos_point(video_len, pos, op_start, op_end)
        
        else :
            pos += 10
            pos = pos_point(video_len, pos, op_start, op_end)            
    return ms_text(pos)
