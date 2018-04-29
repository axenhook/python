innum = 0
list1 = []
while(innum != -1):
    innum = int(input("请输入正整数 (-1：结束)："))
    list1.append(innum)
list1.pop()
print("共输入 %d 个数" % len(list1))
print("最大数为：%d" % max(list1))
print("最小数为：%d" % min(list1))
print("输入数的总和为：%d" % sum(list1))
print("输入数由大到小排序为：{}".format(sorted(list1, reverse=True)))
