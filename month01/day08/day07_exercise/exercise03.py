'''
    dict01 = {"金海":32,"徐天":15,"田丹":0,"柳如丝":500,"铁林":20}
    在字典中找出金条数量最多的人名
    核心思想：
        假设第一个就是最大值
        使用假设的和第二个进行比较, 如果发现更大的, 则替换假设的
        使用假设的和第三个进行比较, 如果发现更大的, 则替换假设的
        使用假设的和进第...个行比较, 如果发现更大的, 则替换假设的
        最后，假设的就是最大的.

'''
dict_person_golds = {"金海": 32, "徐天": 15, "田丹": 0, "柳如丝": 500, "铁林": 20}
# dict --> list --> [(k,v),(k,v)]
list_person_golds = [(name, gold) for name, gold in dict_person_golds.items()]

max_info = list_person_golds[0]
for i in range(1, len(list_person_golds)):
    if max_info[1] < list_person_golds[i][1]:
        max_info = list_person_golds[i]

print("钱最多的是" + max_info[0])

# dict01 = {"金海": 32, "徐天": 15, "田丹": 0, "柳如丝": 500, "铁林": 20}
# dict01 = {gold: name for name, gold in dict01.items()}
# print(dict01[max(dict01.keys())])
