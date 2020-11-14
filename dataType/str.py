#字符串
a = 3
b = '123456'
c = "abc"

print(1+1)
print(b+c) #字符串可以拼接用+号，int整数不能和字符串拼接
#字符串和数字n可以用相乘，表示的是n个字符串
print(b*a)
#如果想拼接字符串和数字，那么需要转化str()函数
print(str(a)+b)#将a转化为字符串
print(a+int(b))#如果字符串b的内部本身是数字，则可以转化为数字

print('c:/note1.txt') #在python中，写文件路径可以用/表示路径

str1 = 'adhgsdsdfs'
print(str1[0])
# len()函数，可以查看字符串的长度
print(len(str1))

#字符串中的切片[起始值：终止值]包含起始值，但是不包含终止值
print(str1[2:5])
#字符串的下标或切片也可以用负数，表示从后向前数
print(str1[-3:]) #终止值为空，表示从起始值到字符串的结束全部都取值
#切片[起始值：终止值：步长]
print(str1[::3])

#index()函数
print(str1.index('h'))  #找到h在字符串里面的下标



list1=[10,20,30,[40,50]]
list2=list1 #普通的赋值,其实list1和list2指向的是同一个内存地址
list2=list1[:] #切片可以生成新的列表,但是对于子列表而言,仍然指向的同一个地址
import copy #导入标准库中的copy模块
list2=copy.copy(list1) #浅拷贝,等价于切片[:]
list3=copy.deepcopy(list1) #深拷贝,list1改变，深拷贝不变
list1[3][0]=60 #修改了list1的值,list2中的值也会跟着改变
print(list1) #[10, 20, 30, [60, 50]]
print(list2) #[10, 20, 30, [60, 50]]
print(list3) #[10, 20, 30, [40, 50]]




