# 找出列表中出现次数最多的元素三种方式

from collections import Counter
words = [
 'my', 'skills', 'are', 'poor', 'I', 'am', 'poor', 'I',
 'need', 'skills', 'more', 'my', 'ability', 'are',
 'so', 'poor'
]
collection_words = Counter(words)
print(collection_words)

#还可以输出频率最大的n个元素,类型为list
most_counterNum = collection_words.most_common(3)
print(most_counterNum)

# 找出列表中出现次数最多的元素
words = [
 'my', 'skills', 'are', 'poor', 'I', 'am', 'poor', 'I',
 'need', 'skills', 'more', 'my', 'ability', 'are',
 'so', 'poor'
]

def maxElement(listA):
    countA = 0
    for word in words:
        tempCount = listA.count(word) #key
        if tempCount > countA:
            countA = tempCount
            elementA = word
    return elementA, countA
print(maxElement(words))

















