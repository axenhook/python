def ctof(c):
    f = c * 1.8 + 32
    return f

inputc = float(input("请输入摄氏温度："))
print("华氏温度为：%5.1f 度" % ctof(inputc))
