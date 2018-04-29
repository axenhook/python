total = person = score = 0
while(score != -1):
    person += 1
    score = int(input("请输入第 %d 位学生的成绩：" % person))
    total += score
average = total / person
print("本班总成绩：%d 分，平均成绩：%5.2f 分" % (total, average))