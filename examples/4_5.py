# ﻿如何对字符串进行左, 右, 居中对齐

data = {
    "Alain": "he is a student",
    "Bob": "he is a doctor",
    "Yjjpp": "he is a agent",
    "HiMiller": "he is leader of nanjing resistance"
}

width = max(map(len, data.keys()))

# 左对齐
for i in data:
    print(i.ljust(width), ":", data[i])

print("-" * 30)
# 右对齐
for i in data:
    print(i.rjust(width), ":", data[i])

print("-" * 30)
# 居中对齐
for i in data:
    print(i.center(width), ":", data[i])

print("-" * 30)
# 左对齐
for i in data:
    print(format(i, "<" + str(width)), ":", data[i])

print("-" * 30)
# 右对齐
for i in data:
    print(format(i, ">" + str(width)), ":", data[i])

print("-" * 30)
# 居中对齐
for i in data:
    print(format(i, "^" + str(width)), ":", data[i])

# Alain    : he is a student
# Bob      : he is a doctor
# Yjjpp    : he is a agent
# HiMiller : he is leader of nanjing resistance
# ------------------------------
#    Alain : he is a student
#      Bob : he is a doctor
#    Yjjpp : he is a agent
# HiMiller : he is leader of nanjing resistance
# ------------------------------
#  Alain   : he is a student
#   Bob    : he is a doctor
#  Yjjpp   : he is a agent
# HiMiller : he is leader of nanjing resistance
