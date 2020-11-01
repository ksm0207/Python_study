def plus(x, y):
    return x + y


def minus(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


saved_value = 0

while 1:

    select_number = int(input("숫자 입력   "))
    saved_value = plus(saved_value, select_number)

    print("저장된 값 = ", saved_value)


from random import *

print("숫자 랜덤 게임")
print("아무 숫자를 3개 입력하세요 (최대 31까지)")

a = randint(0, 9)
b = randint(0, 9)
c = randint(0, 9)

print(a, b, c)


random1 = a
random2 = b
random3 = c


while 1:
    isTrue = 0
    a = int(input("첫번째 숫자 입력 :  "))
    b = int(input("두번째 숫자 입력 :  "))
    c = int(input("세번째 숫자 입력 :  "))

    if a == random1:
        print("첫번째 숫자를 맞췄습니다")
    else:
        isTrue = 1
        print("다시 입력하세요")

    if b == random2:
        print("두번째 숫자를 맞췄습니다")
    else:
        isTrue = 1
        print("다시 입력하세요")

    if c == random3:
        print("세번째 숫자를 맞췄습니다")
    else:
        isTrue = 1
        print("다시 입력하세요")

    if isTrue == 1:
        continue
    else:
        break

