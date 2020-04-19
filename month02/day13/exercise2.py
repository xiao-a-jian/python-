from multiprocessing import Pool
import os

old_folder = "/home/tarena/File/"
new_folder = "/home/tarena/File-备份/"
os.mkdir(new_folder)  # 创建新文件夹


# 复制每一个文件
def copy_file(file):
    fr = open(old_folder+file, 'rb')
    fw = open(new_folder+file, 'wb')
    while True:
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()


def main():
    pool = Pool(4)
    file_list = os.listdir(old_folder)
    for file in file_list:
        pool.apply_async(copy_file, args=(file,))

    pool.close()
    pool.join()


main()








