from random import *

# 유리공격이 드는것, 계란을 치게끔 만드는거
# 유리유지 === 아무것도 안하는거
# 유리방어 : 상대방이 유리를 들었을때 계란 옆을 치는것

print("  너랑나랑 계란깨기  ")
menu = str(input("플레이어 이름을 입력해주세요 : "))
player = menu
computer = ["공격", "유지", "방어"]
user_pattern = ["공격", "유지", "방어"]
u_heart = 3
r_count = 1

print("플레이어 이름 : ", player)
print(f"반갑습니다  {player}  님!!\n시도할수 있는 횟수는 {u_heart}번 입니다")
print(f"{player} 님은 다음과 같은 방법을 사용할수 있습니다 \n ", user_pattern)

check = str(input("계속 진행할까요 ? [y] 버튼을 누르면 대결이 시작됩니다 [n] 또는 [x]를 누르면 종료할수 있어요 !\n"))
if check == "y" or check == "Y":
    print("게임 시작 !!")
    print(f"현재라운드 : {r_count}\n")

while True:
    if check == "n" or check == "N" or check == "x":
        print(check, "을(를) 선택하였습니다 프로그램 종료 ...")
        break

    c_random = randint(0, 2)
    print("컴퓨터는 다음과 같이 시도하였습니다 : ", computer[c_random])
    print(f"{player} : 0번 공격 :: 1번 유지 :: 2번 방어")
    u_random = int(input(user_pattern))

    # 0 컴퓨터가 공격상태 일경우 사용자 방어
    if c_random == 0:
        if u_random == 2:
            print(f"사용자 {user_pattern[2]} 성공 !!\n")
            r_count += 1
            print(f"다음 {r_count}라운드로 가겠습니다 \n ")
        elif u_random == 1:
            print(f" HINT : 컴퓨터가 공격모드 일때는 {user_pattern[1]} 를 해선 안됩니다.\n")
        else:
            u_heart -= 1
            print("패널티 !!!")
            print(f"컴퓨터가 {computer[0]} 모드 일때 맞공격을 해선 안됩니다.")
            print("남은 목숨 ", u_heart, "개\n")

    # 1 컴퓨터가 유지상태 일경우 서로 중립 ?
    if c_random == 1:
        if u_random == 0 or u_random == 1:
            print("")

    # 2 컴퓨터가 방어상태 일경우 사용자 공격
    if c_random == 2:
        if u_random == 0:
            print("공격성공\n")           
        elif u_random == 2:
            print(f" HINT : 컴퓨터가 방어모드 일때는 {user_pattern[2]}를 해선 안됩니다.\n")
        else:
            u_heart -= 1
            print("남은 목숨 ", u_heart, "개\n")

    # 사용자의 목숨이 0 일경우
    if u_heart == 0:
        print(f"{player} 님은 패배하였습니다")
        print(f"최종 라운드는  {r_count}  라운드 입니다 !!")
        break

