"""
文件的拷贝
    有一个文件 timg.jpeg，将其拷贝一份到主目录下，命名为 mm.jpg
"""

fr = open("1.jpeg", "rb")
fw = open("/home/tarena/mm.jpg", "wb")
while True:
    data = fr.read(1024)
    if not data:
        break
    fw.write(data)
fr.close()
fw.close()

