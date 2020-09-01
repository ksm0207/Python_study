# 세트 (set) 집합 이라는뜻
# 집합은 중복이 안되고 순서는 없음

# set 예시

my_set = {1, 2, 3, 3, 3}
print(my_set)  # Result 1,2,3 "3" "3" 중복을 허용하지 않기때문에 뒷부분은 무시 이미 값이 유효함

java_developer = {"Sungmin", "Yeonseo", "Yeonwoo", "Jisoo"}
python_developer = set(["Sungmin", "Dongjin"])

# 교집합 Java와 Python 을 모두 할 수 있는 개발자 출력
print("교집합:", java_developer & python_developer)  # 서로 다른 집합에 있는 항목중에서 똑같은 값이 출력됨
print("교집합:", java_developer.intersection(python_developer))

# 합집합 java 도 할 수 있거나 python 도 할 수 있는 개발자
print("합집합:", java_developer | python_developer)
print("합집합:", java_developer.union(python_developer))  # union : 합집합을 의미함
# 출력은 순서가 크게 상관없으므로 당황하지말것!

# 차집합 (java를 할 수 있지만 python은 할 줄 모르는 개발자)
print("차집합:", java_developer - python_developer)  # java에 있는 내용에서 python 리스트를 뺀다
print("차집합:", java_developer.difference(python_developer))

# python 을 할 줄 아는 사람이 생겼다면?
python_developer.add("Yeonseo")
print("python 개발자 총인원: ", python_developer)

# java를 잊었어요
java_developer.remove("Yeonwoo")
print("java 개발자 현재 남은 인원 :", java_developer)

