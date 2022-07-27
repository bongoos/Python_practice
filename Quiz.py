#Quiz 1 변수를 이용하여 다음 문장을 출력
'''
변수명 : station 
변수값 : "사당", "신도림", "인천공항" 
출력 문장 : xx행 열차가 들어오고 있습니다.
'''
'''
station = "사당"
print(station + "행 열차가 들어오고 있습니다.")
station = "신도림"
print(station + "행 열차가 들어오고 있습니다.")
station = "인천공항"
print(station + "행 열차가 들어오고 있습니다.")
'''



#Quiz2 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
'''
1. 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 한다
2. 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램 작성

조건 1 : 랜덤으로 날짜를 뽑아야함
조건 2 : 월별 날짜는 다름을 감안하여 최소 일수인 28이내로 정함
조건 3 : 매월 1~3일은 스터디 준비를 해야하므로 제외

(출력문 예제)
오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.
'''
'''
 from random import *
 date = randint(4,28)
 # day_offline1 = randint(4,28)
 print("오프라인 스터디 모임 날짜는 매월 "+str(date)+"일로 선정되었습니다.")

나중에 공부해서 다시 풀어보기 반복문 및 제외 함수가 필요할거로 예상
'''




#Quiz3 사이트별로 비밀번호를 만들어주는 프로그램을 작성
'''
예) http://naver.com
규칙 1 : http:// 부분은 제외 => naver.com
규칙 2 : " 처음 만나는 점 (.) 이후 부분은 제외 => naver
규칙 3 : 남은 글자 중 처음 세자리 + 글자 개수 + 글자 내 'e' 개수 + "!"로 구성
                (nav)                 (5)            (1)            (!)
예) 생성된 비밀번호 : nav51!
'''

'''
url = "http://naver.com"
condition = url.replace("http://","")
condition = condition[:condition.index(".")]
password = condition[:3] + str(len(condition)) + str(condition.count("e")) + "!"
print("{0}에 생성된 비밀번호는 {1}입니다.".format(url,password))
'''

'''
url = "http://naver.com"
my_str = url.replace("http://","") #url에서 http://를 제외
# print(my_str)
my_str = my_str[0:my_str.index(".")] # 0~5까지만 나타냄, .이 6번째 자리이고, my_str.index(".") 대신 5를 넣어도 가능 
# print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!" #my_str의 3번째 자리까지 + my_str의 길이 + my_str "e"의 개수 + "!"를 password에 선언
print("{0}의 비밀번호는 {1}입니다." .format(url,password)) #{}를 이용해서 .format의 url과 위에서 선언한 변수 password를 표현
'''


#Quiz4 당신 학교에서는 파이썬 코딩 대화를 주최합니다
'''
참석률을 높이기 위해 댓글 이벤트를 진행하기로 했다.
댓글 작성자들 중 에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 된다.
추첨 프로그램을 작성하시오.

조건1 : 편의상 댓글은 20명이 작성하였고, 아이디는 1~20이라고 가정
조건2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
조건3 : random 모듈의 shuffle과 sample을 활용

(출력 예제)
--- 당첨자 발표 ---
치킨 당첨자 : 1
커피 당첨자 : [2,3,4]
--- 축하합니다 ---

(활용 예제)
from random import *
lst = [1,2,3,4,5]
print(lst)
shuffle(lst)
print(lst)
print(sample(lst,1))
'''

'''
from random import *
#comment = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
comment = range(1,21) #1부터 21직전까지 생성 하지만 type이 range임
comment = list(comment) #list 타입이 필요하므로 변경
shuffle(comment)
winner=sample(comment,4) #4명중에 한명은 치킨, 3명은 커피 중복이 되면 안되므로 한번에 4명 sample함
print(" --- 당첨자 발표 ---")
print("치킨 당첨자 : {0}".format(winner[0]))
print("커피 당첨자 : {0}".format(winner[1:]))
print("--- 축하합니다 ---")
'''

#Quiz 5) 당신은 Cocoa 서비스를 이용하는 택시 기사입니다.
'''
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

조건 1 : 승객별 운행 소요 시간은 5분~50분 사이의 난수로 정해집니다.
조건 2 : 당신은 소요 시간 5분~15분 사이의 승객만 매칭해야 합니다.

(출력문 예제)
[O] 1번째 손님 (소요시간 : 15분) 선택 가능
[] 2번째 손님 (소요시간 : 50분) 선택 불가능
[O] 3번째 손님 (소요시간 : 5분) 선택 가능
~~~
[] 50번째 손님 (소요시간 : 16분)

총 탑승 승객 : 2 분 (예시)
'''

'''
from random import *
cnt = 0 #총 탑승 승객 수
for i in range(1,51): #1~50 승객
    time=randrange(5,51) #5~50분 사이 시간
    if 5 <= time <= 15: #매칭 성공시
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i,time))
        cnt += 1
    else: #매칭 실패시
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i,time))
 
print("총 탑승 승객 : {} 분".format(cnt))
'''


#Quiz6) 표준 체중을 구하는 프로그램을 작성하시오
'''
표준 체중 : 각 개인의 키에 적당한 체중

(성별에 따른 공식)
남자 : 키(m) x 키(m) x 22
여자 : 키(m) x 키(m) x 21

조건1 : 표준 체중은 별도의 함수 내에서 계산
    함수명 : std_weight
    전달값 : 키(height), 성별(gender)
조건 2 : 표준 체중은 소수점 둘째자리까지 표시

(출력 예제)
키 175cm 남자의 표준 체중은 67.38kg 입니다.
'''
'''
def std_weight(height,gender): #m 단위
    if gender == "남자":
        weight = height * height * 22
        return weight
    elif gender == "여자":
        weight = height * height * 21
        return weight

height = int(input()) #cm단위
gender = str(input())
weight = round(std_weight(height / 100 , gender),2) #round()를 이용해 소수점 2째 자리 까지만 표시
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height,gender,weight))
'''

#Quiz7) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
'''
보고서는 항생 아래와 같은 형태로 출력되어야 합니다.

- X 주차 주간 보고 -
부서 : 
이름 : 
업무 요약 : 

1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

조건 : 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만듭니다.
'''

'''
for i in range(1,51):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간 보고 -".format(i))
        report_file.write("\n부서 : ")
        report_file.write("\n이름 : ")
        report_file.write("\n업무 요약 : ")
'''

#Quiz8) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.
'''
(출력 예제)
총 3대의 매물이 있습니다.
강남 아파트 매매 10억 2010년
마포 오피스텔 전세 5억 2007년
송파 빌라 월세 500/50 2000년

[코드]
class House:
    #매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        pass

    #매물 정보 표시
    def show_detail(self):
        pass
'''

'''
class House:
    #매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    #매물 정보 표시
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

houses = []
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House("송파", "빌라", "월세", "500/50", "2000년")
houses.append(house1)
houses.append(house2)
houses.append(house3)

print("총 {0}대의 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.show_detail()
'''

#Quiz9) 동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다.
'''
대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였습니다.
시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오.

조건 1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError로 처리
        출력 메시지 : "잘못된 값을 입력하였습니다."
조건 2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
        치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생시키고, 프로그램 종료
        출력 메시지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."
'''


#코드
'''
class SoldOutError(Exception):
    pass
chicken = 10
waiting = 1
while(True):
    try:
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order > chicken:
            print("재료가 부족합니다.")
        elif order <= 0:
            raise ValueError
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다."\
                .format(waiting, order))
            waiting += 1
            chicken -= order

        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break
'''

#Quiz10) 프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오.
'''
조건 : 모듈 파일명은 byme.py로 작성

(모듈 사용 예제)
import byme
byme.sign()

(출력 예제)
이 프로그램은 나도코딩에 의해 만들어졌습니다.
유튜브 : http://youtube.com
이메일 : nadocoding@gmail.com
'''

import byme
byme.sign()