"""
os模块处理文件
"""
import os

print(os.path.getsize("/home/tarena/LJ/month02/day03/my.log"))  # 获取文件大小

print(os.listdir("."))  # 查看目录中有什么文件

print(os.path.exists("my.log"))  # 文件是否存在

print(os.path.isfile("my.log"))  # 查看 文件是否为普通文件

os.remove("my.log")  # 删除文件
