#스타크래프트를 이용한 class 
#마린 : 공격 유닛, 군인, 총을 쏠 수 있음
'''
name = "마린" #유닛의 이름
hp = 40 #유닛의 체력
damage = 5 #유닛의 공격력

print("{} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))

#탱크 : 공격 유닛, 탱크, 포를 쏠 수 있는데 일반모드/시즈모드
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}".format(tank_hp, tank_damage))

tank2_name = "탱크"
tank2_hp = 150
tank2_damage = 35

print("{} 유닛이 생성되었습니다.".format(tank2_name))
print("체력 {0}, 공격력 {1}".format(tank2_hp, tank2_damage))


def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(\
        name, location, damage))

attack(name, "1시",damage)
attack(tank_name,"1시",tank_damage)
attack(tank2_name,"1시",tank2_damage)  #여러 유닛이면 너무 많이 써야함 -> class를 이용해 틀을 만들어 사용
'''

#class 만들기
#일반 유닛
'''
class Unit:
    def __init__(self,name,hp,damage): #__inti__ : 파이썬에 쓰이는 생성자 함수, 객체가 생성될때 자동으로 호출
        self.name=name                 #객체 : 마린이나 탱크와 같이 클래스로부터 만들어지는 것
        self.hp=hp                     #멤버 변수 : name, hp, damage로 클래스 내에서 만들어지는 변수
        # self.damage=damage
        # print("{0} 유닛이 생성되었습니다.".format(self.name))
        # print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린",40,5) #마린과 탱크는 Unit class의 instance임, 동일한 개수 만큼 개수를 넣어야함. (이름, 체력, 공격력)
marine1 = Unit("마린",40,5) 
tank = Unit("탱크",150,35)

#레이스 : 공중 유닛, 비행기, 클로킹 기능(스텔스)
wraith1 = Unit("레이스",80,5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage)) #클래스 외부에서 작성한 부분, 멤버 변수를 외부에서 사용 가능

#상대방이 토스로 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것
wraith2=Unit("빼앗은 레이스",80,5)
wraith2.clocking = True #객체에 변수를 추가로 할당 가능

if wraith2.clocking == True: #wraith1은 변수를 추가로 할당하지 않았으므로 오류 발생
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

'''

#일반 유닛(부모 클래스)
class Unit:
    def __init__(self,name,hp,speed): #__inti__ : 파이썬에 쓰이는 생성자 함수, 객체가 생성될때 자동으로 호출
        self.name=name                 #객체 : 마린이나 탱크와 같이 클래스로부터 만들어지는 것
        self.hp=hp                     #멤버 변수 : name, hp, damage로 클래스 내에서 만들어지는 변수
        self.speed=speed

    def move(self,location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))
        # self.damage=damage
        # print("{0} 유닛이 생성되었습니다.".format(self.name))
        # print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))


#공격 유닛(자식 클래스)
class AttackUnit(Unit):  #공격유닛은 일반유닛 class로 상속받음 
    def __init__(self,name,hp,speed, damage):   
        Unit.__init__(self, name, hp,speed)      #Unit의 멤버변수를 호출           
        self.damage=damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage)) #이름과 공격력은 위에서 저장한 멤버변수 값 사용

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))
#파이어뱃 : 공격유닛, 화염방사기,
firebat1 = AttackUnit("파이어뱃", 50, 3, 20)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)


#메딕 : 의무병(공격력이 없음)
#드랍쉽 : 공중 유닛, 수송기, 공격기능 없음
#다중 상속 : 부모 클래스가 여러개 있음

#날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable): #두 개의 부모 클래스를 상속받음
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp,0,damage) #지상 speed 0으로 처리
        Flyable.__init__(self, flying_speed)
    
    def move(self, location): #자식 클래스에서 지상 유닛과 공중 유닛 나눠서 정의 가능
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

#발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")

#연산자 오버라이딩 : 자식 클래스에서 하나로 통일

#벌처 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐",80,10,20)

#배틀크루져 : 공중 유닛, 체력과 공격력 높음
battlecrusier = FlyableAttackUnit("배틀크루져",500,25,3)

vulture.move("11시")
battlecrusier.move("9시")

#pass 
#건물
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         pass #아무것도 안하고 넘어간다는 의미(일단 완성된 것 처럼 보임)
 #서플라이 디폿 : 건물, 1개 건물 = 8 만큼의 인구수 생성
#supply_depot = BuildingUnit("서플라이 디폿",500,"7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over()

#super

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        super().__init__(name, hp, 0)
        self.location = location


