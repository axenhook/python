sum = 0
n = int(input("请输入正整数："))
for i in range(1, n+1):
    sum += i
print("1 到 %d 的整数总和为%d" % (n, sum))