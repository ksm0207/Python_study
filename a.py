from random import *

# 유리공격이 드는것, 계란을 치게끔 만드는거
# 유리유지 === 아무것도 안하는거
# 유리방어 : 상대방이 유리를 들었을때 계란 옆을 치는것


computer = ["공격", "유지", "방어"]
user = ["[0] 공격", " [1] 유지", " [2] 방어"]
u_heart = 3
r_count = 1

while True:
    print("게임을 시작하십시오 !")
    c_random = randint(0, 2)
    print("Computer : ", computer[c_random])
    print("사용자 : ", user)
    u_random = int(input(""))

    # 0 컴퓨터가 공격상태 일경우 사용자 방어
    if c_random == 0:
        if u_random == 2:
            print("사용자 방어 성공 !!")
            r_count += 1
            print(f"다음 {r_count}라운드로 가겠습니다 ")
        else:
            u_heart -= 1
            print("남은 목숨 ", u_heart, "개")

    # 1 컴퓨터가 유지상태 일경우 서로 중립 ?
    if c_random == 1:
        if u_random == 0 or u_random == 1:
            print("")

    # 2 컴퓨터가 방어상태 일경우 사용자 공격
    if c_random == 2:
        if u_random == 0 or u_random == 1:
            print("공격성공\n")
        else:
            u_heart -= 1
            print("남은 목숨 ", u_heart, "개")

    # 사용자의 목숨이 0 일경우
    if u_heart == 0:
        print("당신은 패배하였습니다")
        print(f"최종 라운드는  {r_count}  라운드 입니다 !!")
        break

