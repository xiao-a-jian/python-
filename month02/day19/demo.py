"""
界面相互跳转
"""
def fun():
    while True:
        print("二级界面")
        print("")
        print("")
        print("")

        cmd = input("请输入命令：")
        if cmd == "login":
            pass
        elif cmd == "exit":
            break
        else:
            print("请输入正确命令.")



def main():
    while True:
        print("一级界面")
        print("login")
        print("register")
        print("quit")

        cmd = input("请输入命令:")
        if cmd == "login":
            fun()
        elif cmd == "register":
            fun()
        elif cmd == "quit":
            break
        else:
            print("请输入正确命令.")















