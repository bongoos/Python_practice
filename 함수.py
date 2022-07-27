#함수 정의 하는 방법
'''
def open_account():
    print("새로운 계좌가 생성되었습니다.") #정의만 가능하고 호출 실행은 아니다
open_account() #출력하는 방법

def deposit(balance,money): #입금 return을 이용해 값을 반환한다.
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money

def withdraw(balance,money): #출금
    if balance >=money: #잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance-money))
        return balance-money
    else:
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance))

def withdraw_night(balance,money): #수수료가 붙는 출금
    commission = 100 #수수료
    return commission , balance-money-commission #수수료가 얼마 나왔고, 원금-출금-수수료를 튜플 형식으로 반환(,로 구분)

balance = 0 #잔액
balance = deposit(balance, 1000)
#balance = withdraw(balance,500)
commission , balance = withdraw_night(balance,500) #수수료는 100원이고, 500원이 출금 금액이다.
print("수수료는 {0}원이며, 잔액은 {1}원입니다.".format(commission,balance))
'''

#함수에서 기본값 설정
'''
def profile(name, age, main_lang): #\를 이용하여 두 문장으로 표현 가능
    print("이름 : {0}\t나이 : {1}\t 사용 언어 : {2}"\
        .format(name, age, main_lang))

profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")
'''
'''
#같은 학교 같은 학년 같은 반 같은 수업 ->기본 값 활용
def profile(name, age=17, main_lang="파이썬"): #\를 이용하여 두 문장으로 표현 가능
    print("이름 : {0}\t나이 : {1}\t 사용 언어 : {2}"\
        .format(name, age, main_lang))
profile("유재석") #age와 main_lang은 기본값으로 설정되어있음.
profile("김태호")
'''
#키워드 값
'''
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name = "유재석", main_lang="파이썬", age=20) #순서를 바꿔도 키워드에 해당하는 값으로 전달
'''

#가변인자를 이용한 함수호출
'''
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이 : {1}\t".format(name,age),end=" ") #end= " "  : print하고 줄바꿈 하지 않고 이어서 문장 출력
    print(lang1,lang2,lang3,lang4,lang5)
'''
'''
def profile(name, age, *langauge): #*lang은 가변인자로 제한이 없음
    print("이름 : {0}\t나이 : {1}\t".format(name,age),end=" ") #end= " "  : print하고 줄바꿈 하지 않고 이어서 문장 출력
    for lang in langauge:
        print(lang,end=" ")
    print()

profile("유재석",20,"Python","Java","C","C++","C#","JavaScript")
profile("김태호",25,"Kotlin","Swift")
'''

#지역변수와 전역변수
'''
gun = 10 #전역 변수로 사용하면 코드가 복잡해져서 힘듦

def checkpoint(soldiers) : #경계근무
    global gun #전역 공간에 있는 gun 사용 gun=10을 사용
    gun = gun - soldiers #지역변수라 밖에서 사용 불가 
    print("[함수 내] 남은 총 : {0}".format(gun))

#외부에서 gun 정의 완료후 함수 정의에서 변경된 값을 반환해 밖으로 나옴.
def checkpoint_ret(gun,soldiers):
    gun=gun-soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun


print("전체 총 : {0}".format(gun))
#checkpoint(2) #2명이 경계근무 나감
gun = checkpoint_ret(gun,2)
print("남은 총 {0}".format(gun))
'''