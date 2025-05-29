#included[0] = 1항을 의미
#이전 문제에서 배운 인덱스와 값을 동시에 불러오는 enumerate사용하가
# a + d*i(등차수열의 각 항) / (for문을 이용)
#included의 인덱스(i)와 값(b)을 가져와서   
#included[i]가 True이면 해당 인덱스의 a + d*i 값을 answer에 따로 더해 담아줌.
            

def solution(a, d, included):
    answer = 0
    for i, b in enumerate(included):
         if b: answer += (a + d*i)
            
    return answer
