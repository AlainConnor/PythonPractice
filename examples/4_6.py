# ﻿如何去掉字符串中不需要的字符

# 方法一：利用strip()方法
s = "   abc  123   "
print("'", s.strip(), "'")
print("'", s.lstrip(), "'")
print("'", s.rstrip(), "'")

# 方法二：切片+拼接
s = "abc:123"
print(s[0:3] + s[4:])

# 方法三：replace()方法或re.sub()
s = "abc\ndef\tghi\r"
print(repr(s.replace("\n", "")))

import re
print(repr(re.sub("[\n\t\r]", "", s)))

# 方法四：字符串的translate()方法
tables = str.maketrans("", "", "\n\t\r")
print(s.translate(tables))

