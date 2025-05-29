#런타임 에러로 테스트케이스가 일부분만 패스됨.
def solution(code):
    
    mode = 0
    ret=[]
    
    for i, c in enumerate(code):     #range(len(code)) -> enumerate(code)사용 : 인덱스, 값 을 동시에 가져옴. 
        if c == "1":                 # c==1 mode값을 0, 1로 번갈아가며 변경해줌
            mode = 1 - mode
        
        elif (i % 2 == mode):        # mode가 0이면 짝수 인덱스 문자 추가
                ret.append(c)        # mode가 1이면 홀수 인덱스 문자 추가
        
    return "".join(ret) if ret else "EMPTY"    #ret이 비어있지않다면 ret을 join해서 문자열로 반환!
                                               #만약 ret이 비어있다면 EMPTY 반환
    
    ### ret 자체가 이미 bool()함수처럼 동작하기 때문에 bool(ret)처럼 하지않아도
    ### 리스트가 비어있지않으면 True, 리스트가 비어있으면 False로 평가됨.
