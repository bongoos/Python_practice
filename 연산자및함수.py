#연산자
# print(1+1)
# print(3-2)
# print(5*2)
# print(6/3)

# print(2**3) # 2^3=8 n제곱 표시 **
# print(5%3) # % : 나머지 표시, 2   
# print(5//3) # // : 몫, 1
# print(3==3) # == : 앞과 뒤 값이 같다, true
# print(3+4==7) #앞의 연산과 결과가 같다., true
# print(1!=3) # != : 같지 않다, true
# print(not(1!=3)) # 같지 않은 걸 not하므로 false

# print((3>0) and (3<5)) # and 조건 : 모두 true여야 true
# print((3>0)&(3<5)) #and와 동일

# print((3>0)or(3>5)) # or 조건 : 하나만 true면 true
# print((3>0)|(3>5)) # or과 동일 

# print(5>4>3) # true
# print(5>4>7) #false

#수식
# number = 2+3*4
# print(number)
# number = number + 2 #number 변수에 2를 더하는 변수
# print(number)
# number += 2 #위와 동일(줄여서 쓴거)
# print(number)
# number /= 2
# print(number)
# number *=2 #곱하기 나누기 나머지는 소수점자리가 붙음
# print(number)
# number /=2
# print(number)
# number %=2
# print(number)

#숫자처리함수
# print(abs(-5)) #abs()는 절대값, 5
# print(pow(4,2)) #pow()는 n제곱, 4^2=16
# print(max(5,12)) #max()는 최대값으로 , 12
# print(min(5,12)) #min()은 최소값, 5
# print(round(3.14)) #반올림, 3

# #math library 이용
# from math import * #math library를 이용한다는 표시
# print(floor(4.99)) #floor()는 내림,4
# print(ceil(3.14)) #ceil()은 올림, 4
# print(sqrt(16)) #sqrt()은 제곱근, 4

#random 함수
# from random import * #rand 함수 이용하기
# print(random()) #0.0이상 1.0미만 임의의 값 생성
# print(random() * 10) #위의 랜덤하고 다른 함수이므로 다르게 나타남

# name = random() #변수로 나타내면 밑에 두 random함수는 동일
# print(name)
# print(name * 10)

# print(int (random()*10)) #int()는 정수만 표시, 소수점 버리고 *10을 하면 0~10미만 임의값
# print(int(random()*10) + 1) #0을 제외하기 위해 1을 더함, 1부터 10이하의 임의 값

# print(int(random()*45)+1) # 1부터 45이하의 임의의 값
# print(randrange(1,45)) #1부터 45미만 임의의 값
# print(randrange(1,46)) #1부터 45이하 또는 46미만 임의의 값
# print(randint(1,45)) #1부터 45이하 임의의 값

