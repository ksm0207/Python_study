# 사전
# 이번 강의는 사전에서 단어를 검색하면 뜻이 나오듯이 key 와 value를 통해 사전 공부를 해보는것이 목표다
# 사전에서는 키의 중복이 허용되지 않는다
# 예 : 100번방 열쇠 --> (key 라고 가정) 를 받았는데 200번 방을 열수 없듯이 키의 중복은 허용되지 않는다
# key 는 논리적으로 해당되는곳에만 허용된다

# 예시
phone = {1: "iphone8", 100: "iphone8+"}  # {}를 열어 진행 숫자는 key 를 의미하며 다음은 value를 뜻함
print(phone[1], phone[100])

# 사전자료형 가져오는 두가지 방법
print(phone.get(1), phone.get(100))  # get으로 가져오는방법

print(1 in phone)  # 사전자료에 값이 있는지 확인 ket가 phone에 있는지 구체적으로 확인함 결과는 True
print(10 in phone)  # False


# 위의 정수형 으로 아닌 String 으로 값을 가져와보자
phone2 = {"A-201": "iphone8", 100: "iphone8+"}  # {}를 열어 진행 숫자는 key 를 의미하며 다음은 value를 뜻함
print("기존데이터:", phone2)
phone2["A-201"] = "Samsung"  # 기존 key와 value 값 대체
phone2["C-500"] = "Update Object"  # 객체 업데이트
print("변경된데이터:", phone2)

# 사전자료 삭제하기
del phone2["A-201"]
print("남은데이터:", phone2)

# 현재 남은 key값 출력
print("Key:", phone2.keys())

# 현재 value 값 출력하기
print("Value :", phone2.values())

# key value 쌍으로 출력
print("Key + Value = ", phone2.items())

# key value 쌍으로 제거
phone2.clear()
print("남은값 :", phone2)

