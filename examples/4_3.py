# ﻿如何调整字符串中文本的格式

log = "2018-01-10 这是2018年的第一天\n" \
      "2018-03-20 今天开学了\n" \
      "2018-10-01 这是国庆节的第一天"

import re

t1 = re.sub("(\d{4})-(\d{2})-(\d{2})", r"\2/\3/\1", log)
print(t1)

print("-"*40)

t2 = re.sub("(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})", r"\g<month>/\g<day>/\g<year>", log)
print(t2)
