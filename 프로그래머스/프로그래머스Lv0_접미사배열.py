# 빈 리스트 변수생성
# for문 돌면서 맨 앞자리 자른 문자를 리스트에 append함.
# 리스트를 오름정렬함


def solution(my_string):
    answer = []
    for i in range(len(my_string)):
        answer.append(my_string[i:])
        
    return sorted(answer)
