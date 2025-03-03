# 1. range(query[0]:query[1]+1)  
# 2. arr[idx]+1 > query[-1]의 배수일 때



def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        for i in range(s, e+1): 
            if i % k == 0 :
                arr[i] += 1
        
    return arr
