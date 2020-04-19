"""
    练习:在不改变旧功能调用以及定义情况下，为其增加新功能.
        体会"装饰器的拦截"/"闭包的逻辑连续"

    # 新功能
    def verif_permissions():
        print("验证权限")

    # 旧功能
    def enter_background():
        print("进入后台")

    def delete_order():
        print("删除订单")

    enter_background()
    delete_order()
"""


def verif_permissions(func):
    def wrapper(*args, **kwargs):
        print("验证权限")
        return func(*args, **kwargs)

    return wrapper


@verif_permissions
def enter_background():
    print("进入后台")


@verif_permissions
def delete_order():
    print("删除订单")


enter_background()
delete_order()
