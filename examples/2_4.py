# 如何根据字典中值的大小, 对字典中的项排序
from random import randint


# 利用zip函数将字典数据转化为元组，再进行排序
def fun1(data):
    key = data.keys()
    val = data.values()
    new_dict = zip(val, key)
    return sorted(new_dict)


# 利用sorted函数的key参数
def fun2(data):
    new_dict = sorted(data.items(), key=lambda x: x[1])
    return new_dict


if __name__ == "__main__":
    data = {x: randint(80, 100) for x in range(10)}
    print("初始化数据：", data)
    t1 = fun1(data)
    print("利用zip函数：（键值与初始数据对换了位置）", t1)

    t2 = fun2(data)
    print("利用sorted的关键字key：", t2)


