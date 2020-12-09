

from random import randint
import time

class Animal:
    def __init__(self, weight):
        self.weight = weight

    def say(self):
        print('animal say something')
        self.weight -= 5


class Tiger(Animal):
    def __init__(self):
        self.name = 'tiger'
        self.weight = 200

    def eat(self, food):
        if food == 'meat':
            print('喂食正确，体重+10')
            self.weight += 10
        elif food == 'grass':
            print('喂食错误，体重-10')
            self.weight -= 10

    def roar(self):
        print('Wow!!')
        self.weight -= 5

class Sheep(Animal):
    def __init__(self):
        self.name = 'sheep'
        self.weight = 100

    def eat(self, food):
        if food == 'grass':
            print('喂食正确，体重+10')
            self.weight += 10
        elif food == 'meat':
            print('喂食错误，体重-10')
            self.weight -= 10

    def roar(self):
        print('mie~~')
        self.weight -= 5


class Room:
    def __init__(self, category):
        self.category = category

roomlist = []
for i in range(1,11):
    if randint(1,2) == 1:  #结果是1或者2
        category = Tiger() #实例化一个老虎
    else:
        category = Sheep() #实例化一个羊
    rm = Room(category) #将动物放入房间的实例中
    roomlist.append(rm)


startTime = time.time() #距离1970年1月1日的秒数
while time.time() - startTime <= 180:
    num1 = randint(0,9)
    fangjian = roomlist[num1] #随机选择一个房间
    a = input(f'当前访问的是{num1+1}的房间，请问是否需要敲门？Y/n')
    if a == 'Y' or a == 'y':
        fangjian.category.roar() #调用房间实例的动物实例的叫的方法

    b = input('请问是否需要喂食？Y/N')
    if b == 'Y' or b == 'y':
        food = input('请输入需要喂的食物meat/grass')
        if food == 'meat' or food == 'grass':
            fangjian.category.eat(food) #调用房间中动物实例的吃的方法
        else:
            print('食物种类不正确')
else:
    print('游戏时间到')
    for i in range(len(roomlist)):
        print(f'{i+1}号房间的动物是{roomlist[i].category.name}, 体重是{roomlist[i].category.weight}')



