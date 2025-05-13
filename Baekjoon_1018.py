import sys
input = sys.stdin.readline

# N X M
# 체스 색 정보 (W or B)
N, M = map(int, input().split())
min_cnt = 33
# 최소수정횟수 변수 33으로 선언

# 한판넣을변수선언 체스 = 8*8 리스트 
input_C = []
# 2차원리스트로 입력 받기( 라인 M번 반복 )
for i in range(N):
    row_ = input()
    input_C.append(list(row_))

for i in range(N-7):
    for j in range(M-7):
        cnt = 0
        for x in range(8):
            for y in range(8):
                if ((x+y)%2 == 0):
                    if input_C[i+x][j+y] != "B" :
                        cnt +=1
                else :
                    if input_C[i+x][j+y] != "W" :
                        cnt +=1
        if cnt > 32:
            cnt = 64-cnt
        
        if min_cnt > cnt:
            min_cnt = cnt 

print(min_cnt)
