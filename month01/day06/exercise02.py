# 练习：
# 在终端中循环录入内容,如果录入空字符串则停止.
# 打印所有录入的内容(大字符串)

result_list = []
while True:
    message = input("请输入省份名称：")
    if message == "":
        break
    result_list.append(message)
output_message = "-".join(result_list)
print(output_message)
