#패키지 : 모듈들을 모아놓은 집합
'''
import travel.태국 #import는 클래스나 함수를 직접 호출 못하고, 패키지나 모듈만 호출 가능
trip_to = travel.태국.태국패키지()
trip_to.detail()


from travel.태국 import 태국패키지
trip_to = 태국패키지()
trip_to.detail()


from travel import 베트남
trip_to = 베트남.베트남패키지()
trip_to.detail()


from travel import * # *은 모든 것을 가져온다는 의미인데 공개 범위를 설정해줘야한다. 패키지 안에 import 공개/비공개 설정가능
trip_to = 베트남.베트남패키지() 
trip_to = 태국.태국패키지()
trip_to.detail()
'''

#각 파일 위치 확인
from travel import *
import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(태국))