
#一个元素要加逗号
m = (1,)  #一个元素的tuple元组，读成tanple?
n = (1, 'abd', [55, 56])  #不能修改,适用于一组固定元素
print(m, n)

listX = [1, 1.5, 'abc'] #可以增append 删pop 改a[0]=4 查a[2]
tupleY = (1, 1.5, 3, 4, 5, 6)#不能修改
tupleY[0] #查
print(tupleY[0], tupleY[2])

#元组的常用函数
len(tupleY)
max(tupleY)
min(tupleY)
print('len(tupleY): ', len(tupleY), 'max(tupleY): ', max(tupleY),'min(tupleY): ', min(tupleY))

m = 4 in tupleY
print('4 in tupleY or not: ', m) #true

#slice
# 切片
print('tupleY is: ', tupleY)
n = tupleY[0:3]  #0, 1, 2下标
print('tupleY[0:3] is: ',n)

tupleY[1:] #最后一个数字不写的话，默认是下标1到最后一个元素
tupleY[:]# 最前面的元素到最后的元素

print(tupleY[1:], tupleY[:])

