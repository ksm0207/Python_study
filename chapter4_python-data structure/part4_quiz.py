# Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 "1명"은 치킨, "3명"은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하십시오.

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1 ~ 20 이라고 가정합니다.
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복은 불가능합니다.
# 조건3 : random modul의 shuffle 과 sample을 활용하십시오.

# 출력 될 내용
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 [2,3,4]
# -- 축하합니다 ! --

# 활용 예제는 다음과 같습니다.
# from random import *
# list = [1, 2, 3, 4, 5]
# print(list)
# shuffle(list)  # shuffle 은 list의 값을 무작위로 출력합니다.
# print(list)
# print(sample(list, 1))
# sample은 첫번째 인자인 list에서 두번째 인자인 ~개 만큼 sample로 출력합니다.
# 현재 list [1,2,3,4,5] 중에서 1개를 무작위로 출력합니다.

from random import *

# 조건1 만들기
users = range(1, 21)
users = list(users)
shuffle(users)
print(users)
winning = sample(users, 4)
print(winning)

print(" -- 당첨자 발표 --")
print("치킨 당첨자:{0}".format(winning[0]))
print("커피 당첨자:{0}".format(winning[1:]))
print(" -- 축하합니다 --")

# python_developer = set(["Sungmin", "Dongjin"])
# print("교집합:", java_developer & python_developer)  # 서로 다른 집합에 있는 항목중에서 똑같은 값이 출력됨
