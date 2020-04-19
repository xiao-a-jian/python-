from multiprocessing import Pool, Queue
import os

old_folder = "/home/tarena/File/"
new_folder = "/home/tarena/File-备份/"
os.mkdir(new_folder)  # 创建新文件夹

q = Queue()


# 获取文件夹大小
def total_size():
    size = 0
    file_list = os.listdir(old_folder)
    for file in file_list:
        size += os.path.getsize(old_folder + file)
    return size


# 复制每一个文件
def copy_file(file):
    fr = open(old_folder + file, 'rb')
    fw = open(new_folder + file, 'wb')
    while True:
        data = fr.read(1024)
        if not data:
            break
        n = fw.write(data)  # 向目标写入内容
        q.put(n)

    fr.close()
    fw.close()


def main():
    pool = Pool(4)
    file_list = os.listdir(old_folder)
    for file in file_list:
        pool.apply_async(copy_file, args=(file,))

    pool.close()

    all_size = total_size()  # 总大小
    copy_size = 0
    while copy_size < all_size:
        copy_size += q.get()
        print("已拷贝：%.2f%%" % (copy_size/all_size*100))

    pool.join()


main()
