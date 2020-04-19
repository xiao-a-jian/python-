"""
在主目录下有若干个文件和目录，需要删除其中大小不到10个字节的普通文件
"""

import os

dir = "/home/tarena/"

file_list = os.listdir(dir)
for file in file_list:
    if os.path.isfile(dir+file) and os.path.getsize(dir+file) < 10 and file[0] != ".":
        os.remove(dir+file)
