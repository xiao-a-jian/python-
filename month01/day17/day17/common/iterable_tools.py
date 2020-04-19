"""
    可迭代对象的工具模块
"""

# 1. 深刻理解函数式编程思想
# 2. 内置高阶函数有限,自定义工具类可以随着时间推移逐步扩大.
# 3. 参照了微软公司Linq框架思想，而编写的集成操作框架。
class IterableHelper:

    # 做成函数都可以正常工作,如果封装到类中,就是用静态方法.
    @staticmethod  # 数据,逻辑
    def find(iterable, func_condition):
        """

        :param iterable:
        :param func_condition:
        :return:
        """
        for item in iterable:
            if func_condition(item):
                yield item

    @staticmethod
    def find_single(iterable, func_condition):
        """

        :param iterable:
        :param func_condition:
        :return:
        """
        for item in iterable:
            if func_condition(item):
                return item

    @staticmethod
    def get_count(iterable, func_condition):
        """

        :param iterable:
        :param func_condition:
        :return:
        """
        count = 0
        for item in iterable:
            if func_condition(item):
                count += 1
        return count

    @staticmethod
    def select(iterable, func_handle):
        """

        :param iterable:
        :param func_handle:
        :return:
        """
        for item in iterable:
            # yield (item.name,item.face_score)
            # yield (item.height,item.weight,item.face_score)
            yield func_handle(item)

    @staticmethod
    def get_max(iterable, func_handle):
        max_value = iterable[0]
        for i in range(1, len(iterable)):
            # if max_value.face_score < iterable[i].face_score:
            # if max_value.money < iterable[i].money:
            if func_handle(max_value) < func_handle(iterable[i]):
                max_value = iterable[i]
        return max_value

    @staticmethod
    def order_by(iterable, func_handle):
        for r in range(len(iterable) - 1):
            for c in range(r + 1, len(iterable)):
                # if iterable[r].height > iterable[c].height:
                # if iterable[r].weight > iterable[c].weight:
                if func_handle(iterable[r]) > func_handle(iterable[c]):
                    iterable[r], iterable[c] = iterable[c], iterable[r]

    # print(IterableHelper.sum_value(list_wifes, lambda w: w.money))
    @staticmethod
    def sum_value(iterable, func_handle):
        total_value = 0
        for info in iterable:
            total_value += func_handle(info)
        return total_value
