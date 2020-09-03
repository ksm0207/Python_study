# 전달값 and 반환값


def open_account():
    print("새로운 계좌가 생성되었습니다.")


def deposit(balance, money):  # 입금
    print("입금이 완료되었습니다.{0}원".format(balance + money))
    return balance + money


def withdraw(balance, money):  # 출금
    if balance > money:
        print("출금이 완료되었습니다. 잔액은 {0}원 남았습니다.".format(balance - money))
        return balance - money
    else:
        print("잔액이 부족합니다.현재 남아있는 금액 : {0}원".format(balance))
        return balance


def withdraw_night(balance, money):  # 저녁 출금 수수료 증가
    commission = 100  # 수수료
    return commission, balance - money - commission


balance = 0
balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)


commission, balance = withdraw_night(balance, 500)
print("수수료 : {0}원 잔액 : {1}원".format(commission, balance))
