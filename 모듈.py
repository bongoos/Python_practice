#모듈 : 필요한 것들끼리 모여서 만들어진 부품 (함수, 파일명 등을 담고 있고 확장자 : .py)
'''
import 영화모듈
영화모듈.price(3) #3명이서 영화보러 갔을 때 가격
영화모듈.price_morning(4) #4명이서 조조 영화 가격
영화모듈.price_soldier(5) #5명 군인 영화 가격

import 영화모듈 as mv #영화모듈을 mv 별명으로 호출, 위와 동일
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5) 


from 영화모듈 import * #영화모듈 자체를 사용하기
price(3)
price_morning(4)
price_soldier(5)


from 영화모듈 import price, price_morning #명시적으로 필요한 함수만 적어서 사용
price(5)
price_morning(6)
#price_soldier(7) 함수를 불러오지 않았기 때문에 오류 발생

'''

from 영화모듈 import price_soldier as ps #군인 가격을 가져다 쓰는데 ps라는 별명을 이용해 줄여서 사용
ps(5)
