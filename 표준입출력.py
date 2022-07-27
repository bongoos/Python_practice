'''
print("Python","Java") # ,는 한칸 띄어서 출력
print("Python","Java","Javascript",sep=" vs ") #sep = 은 사이에 넣는 값을 설정
print("Python","Java","Javascript",sep=",",end="?")  #end를 이용해 뒷 문장 연달아 한 문장으로 출력
print("무엇이 더 재밌을까요? ") #print()가 두 줄에 걸쳐 나와야하는데 end를 이용해 한줄로 만듦

import sys
print("Python","Java",file=sys.stdout) #표준 출력으로  
print("Python","Java",file=sys.stderr) #표준 에러로 확인을 해서 로깅
'''

'''
scores = {"수학":0,"영어":50,"코딩":100} #Dictionary
for subject,score in scores.items(): #key와 value를 쌍으로 튜플로 보내줌
    #print(subject,score)
    print(subject.ljust(8),str(score).rjust(4),sep=":") #8칸의 공간을 확보한 후 왼쪽 정렬, 4칸의 공간을 확보한 후 오른쪽 정렬
'''

#은행 대기 순번표 (001, 002, 003, ...)
'''
for num in range(1,21):
    print("대기번호 : "+str(num).zfill(3)) #zfill 0을 채운다. 3글자중 빈공간에 대해서 0으로 채운다
'''

'''
answer = input("아무 값이나 입력하세요 : ")
print(type(answer))
print("입력하신 값은 " + answer + "입니다.")  #사용자 입력은 숫자와 문자 모두 str인 문자열로 입력 받는다.
'''

'''
#출력 포맷(빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보)
print("{0: >10}".format(500)) 
#양수일 때는 +로 표시, 음수일 때는 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500)) #맨 윗 문장도 음수 표현 가능하나 양수표현이 불가능
#왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<+10}".format(500))
#3자리마다 콤마를 찍어주기
print("{0:,}".format(1000000000))
#3자리마다 콤마를 찍어주고, +-부호 붙이기 
print("{0:+,}".format(1000000000))
print("{0:+,}".format(-1000000000))
#3자리마다 콤마를 찍어주고, 부호도 붙이고, 자릿수도 확보하기
#돈이 많으면 행복하니까 빈자리는 ^로 채워주기
print("{0:^<+30,}".format(1000000000))
#소수점 출력
print("{0:f}".format(5/3))
#소수점을 특정 자릿수까지만 표시
print("{0:.2f}".format(5/3)) #소수점 3째 자리에서 반올림하기
'''

#파일 입출력
'''
score_file = open("score.txt","w",encoding="utf8") # score.txt파일을 불러오고, w : 쓰기 파일(덮어쓰기), utf8 : 한글 정보 표시
print("수학 : 0 ", file=score_file)
print("영어 : 50",file=score_file)
score_file.close()


score_file = open("score.txt","a",encoding="utf8") #a : 이어서 쓰기(append)
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100") #줄바꿈이 따로 없으므로 \n을 넣어서 줄바꿈 표시
score_file.close()
'''

#한번에 모든 내용 불러오기 가능
'''
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()
'''

#하나씩 불러오기
'''
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(),end="") #줄별로 읽기, 한줄 읽고 커서는 다음줄로 이동, 자동 줄바꿈, end 넣어서 줄바꿈 없애기
print(score_file.readline(),end="")
print(score_file.readline(),end="")
print(score_file.readline(),end="")
score_file.close()
'''
#몇개인지 모르는데 하나씩 불러오기
'''
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line,end="")
score_file.close()
'''

'''
#list를 이용해 불러오기
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()
for line in lines:
    print(line,end="")
score_file.close()
'''