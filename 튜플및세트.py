#튜플 : 변경할 수 없는 자료 구조
'''
menu = ("돈까스","치즈까스")
print(menu[0])
print(menu[1])

#menu.add("생선까스")  -> 튜플은 추가 기능 없음

name = "김종국"
age=20
hobby = "코딩"
print(name,age,hobby)

(name,age,hobby)=("김종국",20,"코딩") #튜플을 이용하면 위와같은 긴 코딩을 한줄로 줄 일 수 있음.
print(name,age,hobby)
'''

#세트(집합), 중복안되고 순서없음
'''
my_set={1,2,3,3,3}
print(my_set) #중복이 안되기 때문에 3이 하나밖에 나타나지 않음

java = {"유재석","김태호","양세형"}
python = set(["유재석","박명수"])

print(java & python) # & : 교집합을 확인
print(java.intersection(python)) #위와 동일한 기능

print(java | python) # | : 합집합을 확인
print(java.union(python)) #위와 동일한 기능             #실행할 때마다 순서가 달라짐 -> 세트는 순서가 없기 때문이다.

#차집합(java는 할 수 있지만 python은 할 줄 모르는 개발자)
print(java-python) #차집합으로 -를 이용해 사용 가능
print(java.difference(python))

#python 할 줄 아는 사람 늘어남
python.add("김태호")  #추가 가능
print(python)

#java를 까먹음
python.remove("김태호") #취소
print(python)
'''


#자료 구조의 변경
menu = {"커피", "우유","주스"}
print(menu,type(menu)) #{}를 이용했기 때문에 set로 이용

menu = list(menu)
print(menu, type(menu)) #list인 []로 감싸 list형으로 변경

menu = tuple(menu)
print(menu, type(menu)) #tuple인 ()로 감싸 tuple형으로 변경

menu = set(menu)
print(menu, type(menu)) #set로 다시 바꿈


