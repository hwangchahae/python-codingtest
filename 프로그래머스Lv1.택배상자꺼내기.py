#+11

def solution(end, w, num):
    
    box_idx = w          # 박스 인덱스 잡기
    if num % w == 0 :
        if ( num // w ) % 2 :
            box_idx = w-1
        else :
            box_idx = 0
    elif (num // w) % 2 :
        box_idx = -(num % w)
    else :
        box_idx = (num % w)-1
        
    
    -(num % w) if (num//w) % 2 else (num % w)-1
    box_list= [ 0 for _ in range(w) ]  # 모든 요소가 0 인 길이 w 리스트 생성
    
    for i in range(num, end+1) :
        if i % w == 0 :                # i가 w의 배수면서
            if (i // w) % 2:           # 몫이 홀수이면
                box_list[w-1] += 1     # 제일 오른쪽 끝 요소 카운팅
            else :                     # 몫이 짝수이면
                box_list[0] += 1       # 왼쪽 끝 카운팅
        
        elif (i // w) % 2 :            # w의 배수가 아니면서
            box_list[-(i % w)] += 1    # 몫이 홀수인 수는 리스트[-나머지]에 카운팅
            
        else :                         # w의 배수가 아니면서 
            box_list[(i % w)-1] += 1   # 몫이 짝수인 수는 리스트[나머지-1]에 카운팅
    
    return box_list[box_idx]           # 상자인덱스에 카운팅 된 수를 반환
