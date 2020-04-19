# 练习1：
#  请排列出所有扑克牌(大小王不算,使用列表存储)
# ["红桃","黑桃","方片","梅花"]
# ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
list_suit = ["红桃", "黑桃", "方片", "梅花"]
list_number = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
list_result = [(suit, number) for suit in list_suit for number in list_number]
print(list_result)
