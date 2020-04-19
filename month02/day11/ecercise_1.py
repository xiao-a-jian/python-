from multiprocessing import Process
import os

filename = "./w.jpg"
size = os.path.getsize(filename)


# 复制上半部分
def top():
    fr = open(filename, 'rb')
    fw = open('top.jpg', 'wb')
    n = size // 2  # 要复制n个字节

    while n > 1024:
        data = fr.read(1024)
        fw.write(data)
        n -= 1024
    fw.write(fr.read(n))
    fr.close()
    fw.close()


def bot():
    fr = open(filename, 'rb')
    fw = open('bot.jpg', 'wb')
    fr.seek(size // 2, 0)
    while True:
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()


p = Process(target=top)
p.start()

bot()

p.join()
