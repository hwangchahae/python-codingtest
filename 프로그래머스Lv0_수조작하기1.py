# control w s d a = 1, -1, 10, -10
# Counter로 등장횟수확인 
# 키값으로 value계산 후 n에 더함.
# control에 따라 n값 변경. 가장 마지막 n값을 return

from collections import Counter

def solution(n, control):
    answer = Counter(control)
    return n + answer["w"] - answer["s"] + (answer["d"] - answer["a"])*10
       
