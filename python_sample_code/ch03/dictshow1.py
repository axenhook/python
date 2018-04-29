dict1={"林小明":85, "曾山水":93, "郑美丽":67}
dict1["黄明品"] = 71
dict1["陈莉莉"] = 98
listkey = list(dict1.keys())
listvalue = list(dict1.values())
for i in range(len(listkey)):
   print("%s 的成绩为 %d 分" % (listkey[i], listvalue[i]))
