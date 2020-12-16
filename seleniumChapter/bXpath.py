
#xpath使用路径表达式来选取xml文档或者HTML文档上的节点或者节点集
#这些路径和我们常规电脑上的文件路径表达式很像

#绝对路径(1个斜杠/  父/子/孙)，是从顶层开始写的，最顶层是一个/，下标是从1开始，每一层都要写出来

#相对路径，是//,两个斜杠，可以跨越层级，//是匹配后代里面满足的元素
#属性定位，
# //div,匹配到所有的div标签
# //div[@class="bar-bottom-wrap"],选取class属性是bar-bottom-wrap的div标签

# 也可以不指定标签类型
# //*[@class="bar-bottom-wrap"],匹配任意类型的标签，且标签的class属性是bar-bottom-wrap

#也可以不指定属性的值
# //*[@class] #匹配所有具备class属性的任意标签

#也可以用and指定多个class属性
# //*[@class="bar-bottom-wrap" and class ="m-contain"]

# 属性加父子关系定位.往上认祖归宗，总能唯一定位
# //div[id="app"]//div[@class="card-main"]

#用.表示自己，用..表示父亲
# //div[id="app"]/..  #找到id是app 的div标签的父亲
# //div[id="app"]/*/* #找到id是app 的div标签的儿子的儿子

#用标签对中间的文本值进行定位，匹配文本是要闻榜的span标签
#//span[text()="要闻榜"]


#匹配所有有文本的span标签，text()方法只能精确匹配，不能模糊匹配
#//span[text()]


#用标签对中间的文本值进行模糊匹配,contains结合text()方法
#//span[contains(text(), "要闻")]