#一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

hei = 100
tour = []
height = []
tim = 10
for i in range(1, tim+1):  #100
    if i == 1:
        tour.append(hei)
    else:
        tour.append(2*hei)
    hei = hei / 2
    height.append(hei)

print(sum(tour), height[-1])
