# if
# weather = input("오늘 날씨가 어때요? ex : 맑음 비 눈 입력 ")
# if weather == "맑음" or weather == "짱": # or 앞 조건 혹은 뒤 조건이 맞을때
# print("놀러 나가기 좋은 날씨군요!")
# elif weather == "비":
# print("우산을 챙겨야 겠네요")
# elif weather == "눈":
# print("빙판길을 조심하세요")
# else:
# print("end")

# 기온예제

temp = int(input("날씨온도 :"))
if 30 <= temp:  # 30 ~31
    print("더운 날씨")
elif 10 <= temp and temp < 30:
    print("좋은 날씨")
elif 5 <= temp < 10:
    print("추운 날씨")
else:
    print("너무 추움")

