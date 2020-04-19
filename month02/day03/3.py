"""
向一个文件中每隔 2秒写入一行内容

         1. 2020-01-01  10:10:10
         2. 2020-01-01  10:10:12
         3. 2020-01-01  10:10:14
         4. 2020-01-01  10:10:16
         5. 2020-01-01  10:15:17
         6. 2020-01-01  10:15:19

         * 写入的内容可以实时看到
         * 程序终止后如果重新启动，序号能够衔接

         温馨提示：  from time import sleep
                    sleep(2)
"""

from time import sleep, ctime

f = open("my.log", "a+", 1)  # 追加，可读

n = 1

# 统计多少行
f.seek(0, 0)  # 文件偏移量放到开头
for line in f:
    n += 1

while True:
    sleep(2)
    msg = "%d.%s\n" % (n, ctime())
    f.write(msg)
    n += 1
