# 문자열 처리 함수

python = "Python is Amazing"
print(python.lower())  # 문자열 소문자 처리
print(python.upper())  # 대문자 처리
print(python[0].isupper())  # Python 문자열의 index 0인 P가 대문자인지 확인함 = True
print(len(python))  # Python의 문자열 길이를 반환 = 17
print(python.replace("Python", "Django"))  # Python 글자를 찾아서 Django로 바꿔서 출력

index = python.index("n")  # Python 의 n의 위치를 찾음
print(index)
index = python.index("n", index + 1)  # 두번째 Amazing 의 n의 위치
print(index)

print(python.find("Django"))  # find()는 Django 라는 값이 없으면 -1을 반환
print(python.index("Django"))  # index()로 Django를 찾으면 에러발생
