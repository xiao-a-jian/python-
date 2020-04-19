# 练习2：对字典进行升序排列{"金海":32,"徐天":15,"田丹":0,"柳如丝":500,"铁林":20}
#              [(k,v),(k,v)]
# list01_dict01 = [(k, v) for k, v in dict01.items()]
# list01_dict01 = [item for item in dict01.items()]

dict01 = {"金海": 32, "徐天": 15, "田丹": 0, "柳如丝": 500, "铁林": 20}
list01 = list(dict01.items())
for r in range(len(list01) - 1):
    for c in range(r + 1, len(list01)):
        if list01[r][1] > list01[c][1]:
            list01[r], list01[c] = list01[c], list01[r]
dict01 = dict(list01)
print(dict01)
