def my_num(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    else:
        return my_num(x-2) + my_num(x-1)

num = []
for i in range(1, 10):
    num.append(my_num(i))
print(num)