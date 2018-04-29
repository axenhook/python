nat = input("请输入语文成绩：")
math = input("请输入数学成绩：")
eng = input("请输入英语成绩：")
sum = int(nat) + int(math) + int(eng)  #输入值需转换为整数
average = sum / 3
print("成绩总分：%d，平均成绩：%5.2f" % (sum, average))