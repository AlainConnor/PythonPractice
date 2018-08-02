# 文件类操作（下）
# 如何使用临时文件

from tempfile import TemporaryFile, NamedTemporaryFile

f = TemporaryFile()
f.write(b"123")
f.seek(0)
s = f.read()
print(s)
f.close()

print()
print("-"*40)
f1 = NamedTemporaryFile()
print("文件目录：", f1.name)
input()
f1.close()



