# List : 순서를 가지는 객체의 집합
# 연속적인 공간을 묶는다고 생각하면되고 그 예시를 들어보자
my_phone = ["아이폰8", "아이폰8+", "아이폰11"]
print("나의 핸드폰은", my_phone[1], "이고", my_phone.index("아이폰8+"), "번째 위치에 있습니다")
# 조건 1 배열속에 객체를 넣고 위치를 찾아보자


# 기기 종류를 추가해보자.
my_phone.append("갤럭시노트20")  # append는 맨뒤에 더한다는 의미
print(my_phone)


# 기기 종류를 아이폰8 / 아이폰8+ 중간에 추가해보자
my_phone.insert(2, "아이폰9")
print(my_phone)


# 기기를 하나씩 뒤에서부터 삭제하기
print("삭제된 객체 : ", my_phone.pop())  # pop은 뒤에서부터 객체를 꺼내는 함수
print("남아있는 객체 :", my_phone)

print("삭제된 객체 : ", my_phone.pop())
print("남아있는 객체 :", my_phone)

print("삭제된 객체 : ", my_phone.pop())
print("남아있는 객체 :", my_phone)

# 같은 기기는 몇대나 있는지 확인하기
my_phone.append("아이폰8+")
print("아이폰8+ : ", my_phone.count("아이폰8+"))

# 객체 정렬하기

food = ["콜라", "사이다", "환타", "핫식스", "커피"]
food.sort()
print(food)

number = [102, 335, 2, 1, 46]
number.sort()
print(number)

# 객체 순서 뒤집기
food.reverse()
print(food)

number.reverse()
print(number)

# 객체 지우기
food.clear()
print(food)
number.clear()
print(food)

# 다양한 자료형 및 리스트 확장
num_list = [5, 2, 4, 3, 1]
mix_list = ["Kim", 26, True]

num_list.extend(mix_list)  # extend 리스트 확장
print(num_list)

