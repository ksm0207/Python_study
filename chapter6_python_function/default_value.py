# 기본값
# 함수에서 기본값을 설정하는것을 배워보자.


def profile(name, age=20, main_lang="Java"):
    print("이름{0} 나이:{1} 사용언어:{2}".format(name, age, main_lang))


user = profile("Kim", "26", "Python + Django")

user_two = profile("Nam")
