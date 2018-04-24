# 如何快速找到多个字典中的公共键
from random import randint, sample
from functools import reduce


# 自定义函数
def fun1(s1, s2, s3):
    res = []
    for x in s1:
        if x in s2 and x in s3:
            res.append(x)
    return res


# 利用map、reduce函数
def fun2(s1, s2, s3):
    dict_map = map(dict.keys, [s1, s2, s3])
    res = reduce(lambda a, b: a & b, dict_map)
    return res


if __name__ == "__main__":
    s1 = {x: randint(1, 4) for x in sample("abcdefg", randint(4, 6))}
    s2 = {x: randint(1, 4) for x in sample("abcdefg", randint(4, 6))}
    s3 = {x: randint(1, 4) for x in sample("abcdefg", randint(4, 6))}
    print("初始化数据：")
    print(s1)
    print(s2)
    print(s3)

    t1 = fun1(s1, s2, s3)
    print(t1)

    t2 = fun2(s1, s2, s3)
    print(t2)
