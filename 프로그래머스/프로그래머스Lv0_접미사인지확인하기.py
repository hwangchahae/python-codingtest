# 빈 리스트 변수생성
# for문 돌면서 맨 앞자리 자른 문자를 리스트에 append함.
# is_suffix을 in을 사용해서 리스트 안에 있는지 확인


def solution(my_string, is_suffix):
    answer = []
    for i in range(len(my_string)):
        answer.append(my_string[i:])
        
    
    return 1 if is_suffix in answer else 0
    
