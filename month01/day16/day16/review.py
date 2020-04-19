"""
    异常
        现象：程序不在向下执行,而是不断返回给调用者.
        目的：异常状态转换为正常状态.
        价值：保障业务流程可以按照既定步骤执行
        手段：
            try:
                可能出错的代码
            except 错误类型 as 别名:
                处理逻辑
    迭代
        可迭代对象:具有__iter__方法,意味着可以参与for
            # for 变量 in 可迭代对象：
            迭代器 = 可迭代对象.__iter__()
            while True:
                try:
                    变量 = 迭代器.__next__()
                except StopIteration:
                    break

        迭代器:具有__next__方法,意味着可以通过一种方式获取数据__next__()
            class XX迭代器：
                def __next__():
                    ...

            class XX可迭代对象:
                def __iter__():
                    return XX迭代器()



"""








