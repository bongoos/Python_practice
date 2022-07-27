class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit,Flyable):
    def __init__(self):
        super().__init__() #부모 클래스의 가장 마지막 클래스만 표현, 순서의 문제가 생김
        Unit.__init__(self)
        Flyable.__init__(self)

#드랍쉽
dropship = FlyableUnit()

