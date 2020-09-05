# 클래스를 만드는 이유 : 유닛은 무한적으로 생산가능하지만 그렇다면 코드를 대량으로 적어줘야한다
# 이런 번거로움을 클래스 라는 틀을 만들어서 코드의 사용을 줄여줄수가 있다.


class Unit:  # 유닛클래스 생성
    def __init__(self, name, hp, damage):
        # init 은 파이썬에서 사용되는 생성자 함수이다
        # 마린 이나 탱크같은 객체들이 만들어질때 호출되는 함수
        # self를 제외한 init 매개변수 만큼 외부에서 똑같이 사용해야함
        self.name = name  # 필요한 값 설정
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다".format(self.name))
        print("체력 {0} 공격력 {1}".format(self.hp, self.damage))


# 외부에서 클래스 사용
# 마린이나 탱크등 클래스로부터 만들어지는애들은 객체라고함
marine = Unit("마린", "45", "6")  # Unit 클래스의 인스턴스
marine2 = Unit("짐레이너", "45", "6")
tank = Unit("탱크", "150", "30")

# Start --> MemberVariable
