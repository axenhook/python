score = input("请输入成绩：")
if(int(score) >= 90):
    print("优秀")
elif(int(score) >= 80):
    print("甲")
elif(int(score) >= 70):
    print("乙")
elif(int(score) >= 60):
    print("丙")
else:
    print("不及格")