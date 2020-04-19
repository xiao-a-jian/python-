"""
    异常处理

    练习1:exercise01
    练习2:对疫情信息管理系统进行异常处理
          保障程序可以按照既定流程进行.
"""


# 语法错误
# 错误(异常)：
# print(qtx)# NameError
# print("成绩："+ 100)# TypeError
# class Wife:
#     pass
# w01  = Wife()
# print(w01.name)# AttributeError

# 运行时错误
# 错误(异常)：
# list01 = [1,2,3]
# print(list01[5])# IndexError

# 写法1：官方建议
def div_apple(apple_count):
    try:
        person_count = int(input("请输入人数："))  # ValueError
        result = apple_count // person_count  # ZeroDivisionError
        print("每人分%d个苹果" % result)
    except ValueError as  e:  # 通过as获取异常对象ValueError
        print("应该输入整数")
        print(e.args)  # 获取异常对象实例变量
    except ZeroDivisionError:
        print("不能输入0")


# 写法2：江湖习惯
# def div_apple(apple_count):
#     try:
#         person_count = int(input("请输入人数："))# ValueError
#         result = apple_count // person_count # ZeroDivisionError
#         print("每人分%d个苹果" % result)
#     # except Exception:
#     except:
#         print("出错啦")

# 写法3：except .. else
# def div_apple(apple_count):
#     try:
#         person_count = int(input("请输入人数："))# ValueError
#         result = apple_count // person_count # ZeroDivisionError
#         print("每人分%d个苹果" % result)
#     # except Exception:
#     except:
#         print("出错啦")
#     else:
#         print("顺利分完了苹果")

# 写法4：try .. finally
# def div_apple(apple_count):
#     try:
#         person_count = int(input("请输入人数："))# ValueError
#         result = apple_count // person_count # ZeroDivisionError
#         print("每人分%d个苹果" % result)
#     # except Exception:
#     except:
#         print("出错啦")
#     finally:# 经常处理收尾工作(一定要做的)
#         print("分苹果结束")


div_apple(10)

print("后续逻辑..")
