#인덱스를 이용해 원소에 접근   -2, -1
#두 원소를 비교 후 
#마직막 원소가 더 크면  마지막 원소 - 그 전 원소 를 추가
#그 전 원소가 크면  마지막원소*2 를 추가

def solution(num_list):
    end = num_list[-1]
    diff = end - num_list[-2]
    num_list.append(diff) if diff > 0 else num_list.append(end*2)
    return num_list
