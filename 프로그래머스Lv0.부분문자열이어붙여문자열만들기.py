# enumerate 이용하여 인덱스와 문자열 받기.
# parts리스트에서 인덱스에 해당하는 parts[i][0]과 parts[i][1]+1 로 슬라이싱해서 
# 공백없이 join 문자열 받고 반환

def solution(my_strings, parts):
    answer=''.join(s[parts[i][0]:parts[i][1]+1] for i, s in enumerate(my_strings))
    return answer
