# 가변인자


def profile(name, age, *add):
    print("이름:{0} 나이:{1}".format(name, age), end=" ")
    for lang in add:
        print(lang, end=" ")
    print()


profile("Kim", 26, "Python", "Java", "C", "PHP", "Android")
profile("Nam", 25, "All")
profile("Seo", 24, "PHP")
profile("Kim", 23, "C", "PHP", "Android")


