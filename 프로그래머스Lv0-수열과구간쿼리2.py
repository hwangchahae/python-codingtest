# 1번째 거르기 arr[query[0]:query[1]+1]  
# 2번째 거르기 arr[idx] > query[-1]
# 3번째 거르기 찾은값중 가장작은값을 넣어줌. 없으면 -1


def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        
        num_list = [n for n in arr[s : e+1] if n > k ]
        answer.append(min(num_list) if num_list else -1)
    return answer
