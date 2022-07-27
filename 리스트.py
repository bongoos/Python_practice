#리스트(순서를 가지는 객체의 집합) []
'''
#지하철 칸별로 10명, 20명, 30명
subway = [10,20,30]
print(subway)

subway = ["유재석","조세호","박명수"]
print(subway)
print(subway.index("조세호")) # .index()를 이용해 0,1,2 중 1번째 위치

subway.append("하하") # .append()는 subway 변수에 객체를 추가하는 함수(맨뒤만 붙음)
print(subway)

subway.insert(1, "정형돈"  ) # .insert(,)는 변수 원하는 위치에 객체를 넣을 수 있음
print(subway)

subway.pop() # .pop()은 맨 뒤의 객체를 빼는 함수
print(subway) 

subway.append("유재석")
print(subway)

print(subway.count("유재석")) #유재석이 몇명있는지 count()를 통해 확인

num_list = [5,2,4,3,1] 
num_list.sort()  # .sort() 순서대로 정렬하는 함수
print(num_list)

num_list.reverse()
print(num_list)  # .reverse() 는 역순으로 정렬하는 함수

num_list.clear() # .clear()은 리스트 안에 있는 객체들 모두 지우기
print(num_list)

mix_list = ["조세호",20,True] #list는 다양한 자료형으로 사용 가능
print(mix_list)

num_list = [5,2,4,3,1]
mix_list = ["조세호",20,True]
num_list.extend(mix_list) # .extend()는 list를 합칠 수 있는 함수
print(num_list)
'''

#사전 {} : key는 중복이 불가

cabinet = {3:"유재석",100:"이광수"}
print(cabinet[3]) #3번인 유재석의 key를 가져옴
print(cabinet[100])
#print(cabinet[5]) #할당이 되어있지않으면 오류가 발생하고 프로그램이 종료됨

print(cabinet.get(3)) #위와 동일
print(cabinet.get(5)) # .get()으로 값을 가져오면 None으로 나타내고 실행 이어서 가능
print(cabinet.get(5,"사용가능")) # 5번이라는 열쇠는 할당이 안되어있으므로 사용가능으로 나타낼 수 있음

print(3 in cabinet) #in을 이용하면 값이 있는지 없는지 확인 가능
print(5 in cabinet)

cabinet = {"A-3" : "유재석", "B-100" : "이광수"}  #숫자뿐만아니라 string(문자열)으로도 사용가능
print(cabinet["A-3"])
print(cabinet["B-100"])

print(cabinet)
cabinet["A-3"] = "지석진" # 같은 key에 새롭게 할당 가능
cabinet["C-20"] = "김종국" # 새로운 key를 할당 
print(cabinet)

del cabinet["A-3"] #A-3에 해당하는 key를 없앰 
print(cabinet) 

print(cabinet.keys()) #key만 확인
print(cabinet.values()) #value만 확인
print(cabinet.items()) #둘다 확인

cabinet.clear()
print(cabinet) #모두 지움

