# 练习：参照以上代码,自定义enumerate(创建生成器函数)
def my_enumerate(list_target):
    index = 0
    for item in list_target:
        yield (index, item)
        index += 1


dict01 = {"张无忌":101,"赵敏":103,"小昭":105}
for item in my_enumerate(dict01):
    print(item)
