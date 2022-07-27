#문자열
'''
 sentence = '나는 소년입니다'
 print(sentence)
 sentence2 = "파이썬은 어렵다"
 print(sentence2)
 sentence3 = """
 나는 소년이고, 
 파이썬은 쉬워요        
 """
 print(sentence3) #""" 를 이용시 여러 문장 한번에 사용 가능
'''

#슬라이싱
'''
jumin = "990312-1401235"   
print("성별 : " +jumin[7]) #[]를 사용하고, index는 0번부터 시작이고, 주민번호의 성별을 나타내는 숫자 위치가 7
print("연 : " + jumin[0:2]) #[0:2]는 년도를 나타내는 숫자는 99인 0부터 1인데 범위는 0부터 2직전까지라는 의미 0~2미만
print("월 : " + jumin[2:4]) #2~3번째 숫자 가져오기
print("일 : " + jumin[4:6]) #4~5번째 숫자 가져오기
print("생년월일 : " +jumin[0:6]) #0~5번째 숫자
print("생년월일 : " +jumin[:6]) #처음부터 시작이면 0을 적지 않아도 무방(처음부터 6직전까지 가져오기)
print("뒤 7자리 : " +jumin[7:14]) #7~13번째 숫자
print("뒤 7자리 : " +jumin[7:]) #7부터 끝까지라는 의미로 0을 적지 않아도 무방 
print("뒤 7자리(뒤에서 부터) : " + jumin[-7:]) #맨 뒷자리는 -1부터 시작 (중요), 0이 끝이 아니고 -1임, 맨뒤에서 7번째까지
'''

#문자열 처리함수
'''
python = "Python is Amazing"
print(python.lower()) #.lower()함수는 전체 문장을 소문자로 바꾸는 함수
print(python.upper()) #.upper()함수는 전체 문장을 대문자로 바꾸는 함수
print(python[0].isupper()) #python의 첫번째 알파벳이 대문자인가 확인, True
print(python[3].islower()) #python의 4번째 알파벳이 소문자인가 확인, True
print(len(python)) #python의 길이를 나타냄, 띄어쓰기 포함
print(python.replace("Python","Java")) #.replace(,)는 앞의 단어를 찾아 뒤의 단어로 바꾸는 함수

index = python.index("n") #n이 python에서 몇 번째에 있는지 확인하는 함수
print(index)
index = python.index("n", index + 1) #첫번째 n이 저장된 index부터 다음 python에서의 n이 몇 번째인지 확인하는 함수 
print(index)

print(python.find("n")) # index와 비슷
print(python.find("Java")) #존재하지 않기 때문에 -1로 반환
#print(python.index("Java")) #존재하지 않기 때문에 에러를 반환 -> find()와의 차이 그 뒤부터 오류때문에 진행이 불가
print(python.count("n")) #n이 총 몇번 존재하는지 확인하는 함수
'''

#문자열 포맷
'''
print("a" + "b")
print("a","b")
#방법 1
print("나는 %d살입니다." %20 ) # %d는 정수값만 가능하고, 뒤의 숫자를 문장에 넣는 역할
print("나는 %s을 좋아해요." %"파이썬") # %s는 string값으로 문자열을 문장에 넣는 역할
print("Apple은 %c로 시작해요." %"A") # %c는 character라 한 글자만 받아 넣는 역할

print("나는 %s살입니다." %20 )  # %s는 정수, 문자, character 모두 사용 가능
print("나는 %s을 좋아해요." %"파이썬") 
print("Apple은 %s로 시작해요." %"A")

print("나는 %s색과 %s색을 좋아해요."%("파란", " 빨간"))  # %괄호안에 컴마를 사용해서 여러개의 문자를 넣을 수 있는 역할

#방법 2
print("나는 {}살입니다.".format(20)) #{}를 이용해서 .format()안에 들어가는 숫자를 넣는 역할
print("나는 {}색과 {}색을 좋아해요".format("파란","빨간")) #동일하게 컴마를 이용해서 사용
print("나는 {0}색과 {1}색을 좋아해요".format("파란","빨간")) #0에 첫번째 파란, 1에 두번째 빨간 넣는 역할
print("나는 {1}색과 {0}색을 좋아해요".format("파란","빨간")) #순서에 따라 바꿔서 넣을 수 있음

#방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color="빨간")) #변수처럼 선언하여 값을 넣을 수 있음
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간",age = 20)) #순서가 달라도 변수에 맞는 값을 넣음 

#방법 4
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요") #f부터 적으면 실제 변수에 저장된 값을 넣음
'''

#탈출 문자
'''
print("백문이 불여일견 \n백견이 불여일타") #\n은 줄바꿈을 의미
#print("저는 "나도 코딩"입니다.") # ""를 감싸는 문장은 하나의 문자열로 인지해 오류 발생
print("저는 '나도 코딩'입니다.") #''를 사용해서 사용 가능 그러나 큰따옴표 불가
print('저는 "나도 코딩"입니다.') #''를 먼저 사용하면 큰따옴표로 사용가능 ->어색함
print("저는 \"나도 코딩\"입니다.") #\"    \"사이에 넣으면 문자열 인지가 아닌 그냥 문자로 인식
print("저는 \'나도 코딩\'입니다.") #\'    \'도 동일

# \\ : 문장 내에서 하나의 \로 바뀜
#print("C:\Users\kbh99\OneDrive\바탕 화면\pythonwork space>") # \는 탈출문자도 아니고 오류가 나는 상황
print("C:\\Users\\kbh99\\OneDrive\\바탕 화면\\pythonwork space>")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") #\r을 통해 그 뒤의 문장이 맨 앞으로 이동, 근데 4글자밖에 적용이 안되네?

# \b : 백스페이스(한 글자 삭제)
print("Redd\bApple") #\b는 뒤의 글자를 지우는 역할, 백스페이스 역할과 동일

# \t : 탭 역할 4칸씩 이동
print("Red\tApple")
'''