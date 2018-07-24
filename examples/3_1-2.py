# 如何实现迭代器对象和可迭代对象

import requests
from collections import Iterable, Iterator


def getweather(city = "天津"):
    url = "http://wthrcdn.etouch.cn/weather_mini?city="
    html = requests.get(url + city)
    data = html.json()["data"]["forecast"][0]
    print(data["low"],data["high"])

# getWeather("天津")
# getWeather("北京")
# getWeather("南京")

class weatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def getWeather(self, city):
        url = "http://wthrcdn.etouch.cn/weather_mini?city="
        html = requests.get(url + city)
        data = html.json()["data"]["forecast"][0]
        return "%s,%s,%s" % (city, data["low"], data["high"])

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getWeather(city)


class weatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return weatherIterator(self.cities)


w1 = weatherIterator(["天津", "北京", "南京"])
w2 = weatherIterable(["天津", "北京", "南京"])

for i in w1:
    print(i)

print("-"*20)

for i in w2:
    print(i)

# 天津,低温 24℃,高温 28℃
# 北京,低温 24℃,高温 28℃
# 南京,低温 28℃,高温 35℃