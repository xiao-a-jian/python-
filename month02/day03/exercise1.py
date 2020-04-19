#!/usr/bin/python3

def cat(file):
    try:
        f = open(file)  # 默认以读方式打开
    except Exception:
        print("没有文件")
    else:
        while True:
            data = f.read(1024)
            if not data:
                break
            print(data)

        f.close()


file = input(">>")  # 输入一个文件名
cat(file)  # 将文件名传给函数参数
