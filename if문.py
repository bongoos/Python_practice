#if문을 이용해 날씨에 따른 변경
'''
weather = input("오늘 날씨는 어때요? ") #input() : 문자열 형태로 입력 받고 저장
if weather =="비" or weather =="눈":
    print("우산을 챙기세요")
elif weather == "미세먼지" :
    print("마스크를 챙기세요")
else : 
    print("준비물이 필요 없어요")
'''

#if문을 이용해 기온에 대해 변경
'''
temp = int(input("기온은 어때요? "))
if 30 <= temp : 
    print("너무 더워요. 나가지 마세요")
elif 10 < temp < 30 :
    print("괜찮은 날씨에요")
elif 0 < temp <10 : 
    print("외투를 챙기세요")
else :
    print("너무 추워요. 나가지 마세요")
'''

#반복문을 이용한 대기
'''
for waiting_no in [0,1,2,3,4] :   #for을 이용해 반복
     print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(5) :   #for을 이용해 반복 range() 0~4까지 출력
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(1,6) :   #for을 이용해 반복 range() 1~5까지 출력
    print("대기번호 : {0}".format(waiting_no))


starbucks = ["아이언맨","토르","아이엠 그루트"]
for customer in starbucks :
    print("{0}, 커피가 준비되었습니다.".format(customer))
'''


