# 文件类操作（上）

# 写入文件和读出文件
filePath = "../tmp/fileOpr.txt"
f = open(filePath, "wt", encoding="utf8")
f.writelines(["I like Python.\n", "我喜欢编程。"])
f.close()

f = open(filePath, "rt", encoding="utf8")
for i in f.readlines():
    print(i)
f.close()

f = open(filePath, "r", encoding="utf8")
print(f.readlines())
f.close()

import array
# 二进制文件的读写
import struct

wavPath = "../tmp/传奇.wav"
newMusicPath = "../tmp/新传奇.wav"
f = open(wavPath, "br")
info = f.read(44)

numChanel = struct.unpack("h", info[22:24])
print("声道数：", numChanel)

totalLen = f.seek(0, 2)
dataLen = (totalLen - 44) // 2

buf = array.array("h", [])
f.seek(44)
buf.fromfile(f, dataLen)
f.close()

for i in range(dataLen):
    buf[i] //= 8

f2 = open(newMusicPath, "wb")
f2.write(info)
buf.tofile(f2)
f2.close()
