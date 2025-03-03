import math

def solution(num_list):
    
    num_prod = math.prod(num_list)
    num_sum2 = pow(sum(num_list), 2)
    
    return 0 if num_prod > num_sum2 else 1
