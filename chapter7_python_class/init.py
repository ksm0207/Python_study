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


# 마린이나 탱크등 클래스로부터 만들어지는애들은 객체라고함
marine = Unit("마린", "45", "6")  # Unit 클래스의 인스턴스
marine2 = Unit("짐레이너", "45", "6")
tank = Unit("탱크", "150", "30")
