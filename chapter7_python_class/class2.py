# 클래스를 만드는 이유 : 유닛은 무한적으로 생산가능하지만 그렇다면 코드를 대량으로 적어줘야한다
# 이런 번거로움을 클래스 라는 틀을 만들어서 코드의 사용을 줄여줄수가 있다.


class Unit:  # 유닛클래스 생성
    def __init__(self, name, hp, damage):
        self.name = name  # 필요한 값 설정
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다".format(self.name))
        print("체력 {0} 공격력 {1}".format(self.hp, self.damage))


# 외부에서 클래스 사용
marine = Unit("마린", "45", "6")
marine2 = Unit("짐레이너", "45", "6")
tank = Unit("탱크", "150", "30")

