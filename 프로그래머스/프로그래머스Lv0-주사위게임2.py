#다른 숫자가 나옴에 따라 더할지, 제곱값을 더할지, 세제곡값을 더할지 나눠짐.
#set은 중복을 허용하지않으니
#set에 a,b,c를 넣고 set에 길이에 따라 연산해줌.
#pow() 연산을 사용

def solution(a, b, c):
    answer = 1
    num_list = [a, b, c]
    num_set = {a, b, c}
    n = len(num_list) - len(num_set) + 1
    
    for i in range(n):
        answer *= (pow(a, i+1) + pow(b, i+1) + pow(c, i+1))        
    
    return answer
