# 如何统计序列中元素的出现频度
from random import randint
from collections import Counter
import re


# 自己编写函数解决问题
def fun1(data, *, k=3):
    c = dict.fromkeys(data, 0)
    for x in data:
        c[x] += 1
    d = sorted(c.items(), key=lambda item: item[1], reverse=True)
    # return {k: v for k, v in d[0:k]}  # 以字典形式输出
    return d[0:k]  # 以列表形式输出


# 使用collections中的Counter类（专门用来统计词频的一个函数）
def fun2(data, *, k=3):
    c = Counter(data)
    return c.most_common(k)


def readfile(filePath):
    txt = open(filePath).read()
    return txt


if __name__ == "__main__":
    # 准备数据
    data = [randint(0, 10) for _ in range(20)]
    print("初始化数据：", data)

    # 选出出现次数最多的4中元素，并已字典的形式输出
    t1 = fun1(data, k=4)
    print(t1)

    t2 = fun2(data, k=4)
    print(t2)

    # 对文本文件进行词频统计,找出词频最高的10个单词
    txt = readfile("../tmp/CodingStyle.txt")
    wordList = re.split("\W+", txt)
    t3 = fun2(wordList, k=10)
    print(t3)
