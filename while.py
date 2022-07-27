#while : 조건이 만족할 때까지 반복
'''
customer = "토르"
index = 5
while index >= 1 :
    print("{0}, 커피가 준비되었습니다. {1} 번 남았습니다.".format(customer,index))
    index -= 1
    if index == 0 :
        print("커피는 폐기처분되었습니다.")
   

#무한 루프
customer = "아이언맨"
index = 1
while True : 
    print("{0}, 커피가 준비되었습니다. 호출 {1} 회".format(customer,index))
    index += 1
'''

#무한루프 탈출
'''
customer = "토르"
sales = "Unknown"

while sales != customer :
    print("{0}, 커피가 준비되었습니다.".format(customer))
    sales = input("이름이 어떻게 되세요?")
print("여기 있습니다. 맛있게 드세요")
'''

#continue와 break (학생들에게 책을 읽도록)
'''
absent = [2,5] #결석한 친구
no_book = [7]
for student in range(1,11): #1~10까지 번호가 있음
    if student in absent :
        continue #여기 위치에 있어서 결석한 학생이라면 밑에 문장 실행하지 않고 다시 for문 처음으로 돌아간다.
    elif student in no_book :  
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break # break를 이용해 그 뒤에 어떤 값이 있는지 상관없이 반복문을 끝냄
    print("{0}, 책을 읽어봐".format(student))


#한줄 for문
#출석번호가 1,2,3,4 앞에 100을 붙이기로 함 - > 101,102,103,104
student = [1,2,3,4,5]
print(student)
student = [i+100 for i in student]  #student에 값을 i에 하나씩 불러와서 100을 더하고 결과
print(student)
'''

#학생 이름을 길이로 변환
student = ["Iron man", "Thor", "I am groot"]
student = [len(i) for i in student] #student를 i에 조회하면서 그 i의 길이를 출력
print(student)

#학생 이름을 대문자로 변환
student = ["Iron man", "Thor", "I am groot"]
student = [i.upper() for i in student] #student를 i에 조회하면서 그 i의 길이를 출력
print(student)