# 如何拆分包含多种分隔符的字符串

str = "abc,de,,fg;hi|jk|lmno\tpqrs\ttuvwxyz"


def mySplit(s, ds):
    res = [s]
    for d in ds:
        t = []
        # python3中map产生了一个生成器，只有在迭代的时候才会调用lambda函数
        list(map(lambda x: t.extend(x.split(d)), res))
        res = t
    return [x for x in res if x]  # 删掉空字符串，否则两个连续逗号间会产生一个空字符串""


print(mySplit(str, ",;|\t"))

import re

print(re.split("[,;|\t]+", str))
