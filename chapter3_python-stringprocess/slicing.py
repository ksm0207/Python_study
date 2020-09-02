# 슬라이싱

# 슬라이싱 이란 문자열에 필요한 정보를 잘라서 사용하는것
jumin = "950207-1234567"

print("성별:", jumin[7])
print("연:", jumin[0:2])  # 0부터 2직전까지 (index : 0,1)
print("월:", jumin[2:4])
print("일", jumin[4:6])

print("생년월일:", jumin[0:5])
# print("생년월일:", jumin[:6]) # 처음부터 6직전까지 가져옴

print("뒤 7자리:", jumin[7:14])
print("뒤 7자리:", jumin[7:])  # 7부터 끝까지

# print("뒤 7자리 (뒤에부터): ", jumin[-7:]) 맨 뒤에서 7번째부터 끝까지 출력

