#78 题目：找到年龄最大的人，并输出。请找出程序中有什么问题。

if __name__ == '__main__':
    person = {"li": 18, "wang": 50, "zhang": 20, "sun": 22}

    def find_max(dict):
        max_age = 0
        for key, value in dict.items():
            if value > max_age:
                max_age = value
                name = key
        print(name)
        print(max_age)
    find_max(person)


