# 클래스는 스타크래프트로 예시로 들어서 진행함
# 마린 : 공격유닛 , 군인 , 총

name = "마린"  # 유닛의 이름
hp = 40  # 유닛의 체력
damage = 5  # 유닛의 공격력

print("{} 유닛이 생성되었습니다".format(name))
print("체력{0},공격력{1}\n".format(hp, damage))

# 탱크 : 공격유닛 , 탱크 , 포를 쏠 수 있음 / 일반모드 / 시즈모드

tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{} 유닛이 생성되었습니다".format(tank_name))
print("체력{0},공격력{1}\n".format(tank_hp, tank_damage))

# 두 유닛은 공격이 가능하므로 함수를 만든다


def attack(name, location, damage):
    print("{0} : {1} 방향으로 적을 공격합니다.[공격력 {2}]".format(name, location, damage))


attack(name, "1시", "5")
attack(tank_name, "1시", "20")

# 클래스를 만드는 이유 : 유닛은 무한적으로 생산가능하지만 그렇다면 코드를 대량으로 적어줘야한다
# 이런 번거로움을 클래스 라는 틀을 만들어서 코드의 사용을 줄여줄수가 있다.
