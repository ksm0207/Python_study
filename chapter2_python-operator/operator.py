# 연산자

print(1 != 3)  # 1이 3이랑 일치하지 않냐? True

# not not은 뒤에있는 데이터와 반대 의미를 뜻한다
print(not (1 != 3))  # 1은 3과 일치하지않은 True이지만 결과는 False가 나옴
print((3 > 0) and (3 < 5))  # and는 양옆의 데이터가 유효할때만 조건이 발동된다. &&

print((3 > 0) | (3 < 5))  # 둘중 하나라도 True이면 or 조건이 발동됨

