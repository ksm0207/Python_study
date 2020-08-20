# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# 예) http://naver.com

# 규칙 1 : http:// 부분은 제외 => naver.com 출력
# 규칙 2 : 처음 만나는 점 (.) 이후 부분은 제외 => naver 출력
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
#                  (nav)                (5)             (1)        (1)
# 생성된 비밀번호 : nav51!

url = "http://google.com"

exist = url.replace("http://", "")
print(exist)
exist = exist[:6]
print(exist)
g_password = exist[:3] + str(len(exist)) + str(exist.count("e")) + "!"

print("{url} 의 비밀번호는 {g_password} 입니다".format(url=url, g_password=g_password))


# email = "http://naver.com"
# my_str = email.replace("http://", "")  # 규칙1
# print(my_str)
# my_str = my_str[:5]  # 규칙 2
# print(my_str)

# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"  # 규칙3
# print(password)

# print("{email} 의 비밀번호는 {password} 입니다.".format(email=email, password=password))

