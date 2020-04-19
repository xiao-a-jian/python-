"""
    字符串字面值
        单双三引号
        转义符
        格式化字符串
    练习:exercise06
"""
# 1. 字符串各种写法
# 双引号
message = "我叫qtx."
# 单引号
message = '我叫qtx.'
# 三引号：可见即所得
message = '''我叫
qt
x.'''
print(message)
message = """我叫qtx."""

#  单引号内的双引号不算结束符
#  双引号内的单引号不算结束符
message02 = '我叫"qtx".'
message02 = "我叫'qtx'."
message02 = """我叫'q't"x"."""

# 2. 转义符:  改变 原始含义 的特殊符号
# \"   \'    \\   \t 水平制表格tab键   \n 换行
message03 = "我叫\"qtx\"."
url = "C:\\antel\\bogs\\c\\d.txt"
url = r"C:\antel\bogs\c\d.txt"
print(url)

message03 = "我叫\tqtx."
message03 = "我叫\nqtx."
print(message03)

# 3.　字符串格式化
#     "..占位符1..占位符2.."%(变量1,变量2)
# 占位符：字符串%s　　整数%d   小数%f
# 字符串拼接
subject = "I"
predicate = 1 + 1
object = 8.382
print("主语：%s,谓语:%d,宾语:%.2f" % (subject, predicate, object))
