# 덧셈
def plus(x, y):
    return x + y


# 뺄셈
def minus(x, y):
    return x - y


# 곱셈
def multiply(x, y):
    return x * y


# 나눗셈
def division(x, y):
    return x / y


while True:
    print("사칙연산 계산기 [1] 덧셈 [2] 뺄셈 [3] 곱셈 [4] 나눗셈 [5] 종료하기")
    select_menu = int(input("원하는 번호를 골라주세요"))
    if select_menu <= 4:
        select = int(input("첫번째 숫자 입력"))
        select2 = int(input("두번째 숫자 입력"))
        if select_menu == 1:
            plus_value = plus(select, select2)
            print("결과는 : %d 입니다." % plus_value)
        elif select_menu == 2:
            minus_value = minus(select, select2)
            print("결과는 : %d 입니다." % minus_value)
        elif select_menu == 3:
            multiply_value = multiply(select, select2)
            print("결과는 : %d 입니다." % multiply_value)
        elif select_menu == 4:
            division_value = division(select, select2)
            print("결과는 %d 입니다" % division_value)
    elif select_menu == 5:
        print("프로그램을 종료합니다")
        break
