def solution(num_list):
    even = 0
    odd = 0
    
    for n in num_list:
        if n % 2 == 0 :
            even = even*10 + n 
        else :
            odd = odd*10 + n 
    
    answer = even+odd
    return answer



# 계속 점수가 1, 아니면 2씩만 올라가길래 챗GPT한테 이유를 물어봤다.
# 단지 풀기만하는게 아니라 복잡성, 효율성을 고려해야 높은 점수를 주나보다.
# 어떻게하면 효율적인지 문제를 알려주고 내가 작성한 코드를 보여주면서 코드수정을 요청했다.
# 제한사항이 1~9이기때문에 굳이 문자열로 변화하고 다시 정수형으로 변환하는게 비효율이라고한다.
# 와.... 진짜 그렇다...
# 이어붙여야한다면 10씩 곱하는 방법을 왜 몰랐을까 그럼 자료형을 계속 변환하지 않아도 될텐데
# 앞으로는 무작정 풀기보다 조금더 효율성있는 코드를 써보려고 노력해야겠다.
