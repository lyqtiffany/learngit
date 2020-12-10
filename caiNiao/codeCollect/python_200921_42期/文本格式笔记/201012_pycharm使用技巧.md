```python
#201012_pycharm使用技巧
#设置新建文件时的自动生成的代码或注释
#settings→editor→file and code templates
#比如输入#${NAME} 当前文件名,#${DATE} 当前日期

#自动补齐
#输入main然后按tab键,就会自动补齐if __name__ == '__main__': 语句

#自定义自动补齐段落
#settings→editor→live templates,在页面右侧点击+号,新增自定义的内容
#记得选择生效的范围


#修改函数的颜色
#settings→editor→color scheme→python→function call(调用函数时的颜色)
#settings→editor→color scheme→python→function definition(调用函数时的颜色)

#设置分屏的快捷方式
#settings→keymap,然后查询split关键字,就可以设置快捷键了
#vertically 纵向切割,horizontally 横向切割

#版本管理svn,cvs,git
#选择一个文件,右键,选择Local history,然后选择show history
#在文件历史列表中,右键,然后点击revert,就可以进行回退

#一些常见的快捷键
#先输入main,然后ctrl+J,然后回车
#快速切入到下一行,shift+回车
#快速注释,ctrl+/ ,再按一次就是取消注释
#tab键,向后缩进4个空格,shift+tab,取消缩进

#编码问题
#settings→editor→file encoding,根据需要进行设置



#冒泡算法与调试
# list1=[158, 86, 454, 29, 180, 412, 20, 481, 353, 208]
#列表自带的排序方法
# list1.sort()  #永久排序
# list1.sort(reverse=True)  #倒序
# list2=list1[::-1]  #翻转
# print(list2)
# print(list1)
# print(sorted(list1))  #临时排序

# for i in range(len(list1)):
#     for j in range(len(list1)-1-i):
#         if list1[j]>list1[j+1]:
#             # print(f'第{j}位和第{j+1}位的顺序不对')
#             # print(f'变化之前------>{list1}')
#             list1[j],list1[j+1]=list1[j+1],list1[j]
#             # print(f'变化之后------>{list1}')
# print(list1)
```