# 다시 풀어본 코드

# for -> while로 대체
# while의 조건은 몫이 0이 아닐때까지 반복으로 설정 
# 나머지를 리스트에 넣고 
# 몫은 num에 재 할당
# 반복문이 종료된 후 리스트 순서를 역으로 바꿔줌
# 리스트요소들을 ','를 기준으로 조인함.
# +++++join은 문자열 리스트만 처리가능함
# +++++input으로 사용자에게 입력값을 받는코드로 변경
# +++++.rjust()함수로 나머지가 2자리일때 맨앞에 0을 추가해서 3자리로 맞춰 리스트에 넣어줌

num = int(input('정수를 입력해주세요 : '))
price = []

while (num//1000) != 0 :
  if num % 1000 == 0 :
    price.append(str(num % 1000).rjust(3, "0"))
  else :
    price.append(str(num % 1000))
  num //= 1000

price.append(str(num))

price.reverse()
print(','.join(price))
