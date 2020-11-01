from random import *

lists = []

ran_num = randint(0, 9)

for i in range(3):
    while ran_num in lists:
        ran_num = randint(0, 9)
    lists.append(ran_num)


print(lists)

while True:

    input1 = int(input("첫번째 숫자 입력  "))
    input2 = int(input("두번째 숫자 입력  "))
    input3 = int(input("세번째 숫자 입력  "))

    input_list = [input1, input2, input3]

    s = 0

    b = 0
    for i in range(len(lists)):
        for j in range(len(input_list)):
            if i != j:
                if input_list[j] == lists[i]:
                    b += 1
            else:
                if input_list[j] == lists[i]:
                    s += 1

    print("s:: ", s, "  b:: ", b)

