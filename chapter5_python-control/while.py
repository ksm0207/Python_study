# while

# 예시 : 어떤 커피점에는 5번의 손님을 호출하고 이에 응답하지 않으면 커피를 처분하도록 하자

# guest = "Kim"
# index = 5  # 5번인지 확인하기 위한 변수
#
# while index >= 1:  # while 문은 조건이 만족할때까지 실행함 index가 1보다 크거나 같을때까지 진행
# print("{0}님 커피가 완료되었습니다. {1}번 호출".format(guest, index))
# index -= 1  # 실행할때마다 -= 1씩 감소
# if index == 0:
# print("처분")
#


guest = "Kim"
person = "Null"

while person != guest:
    print("커피가 준비되었습니다")
    person = input("이름이 뭐예요? ")
    if person != guest:
        print("{0}:  올바르지 않은 요청입니다.".format(person))
    elif person == "Kim":
        print("{0} 님 커피를 받아주세요!".format(person))
