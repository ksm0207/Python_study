# continue

absent = [2, 5]  # 결석한 사람
no_book_stduent = [7]
for student in range(1, 11):
    if student in absent:
        continue  # continue 를 만나면 아래 코드는 실행하지 않고 반복문을 이어간다
    elif student in no_book_stduent:
        print("수업 종료 {0} 은 교무실로 오세요".format(student))
        break
    print("{0}".format(student))
