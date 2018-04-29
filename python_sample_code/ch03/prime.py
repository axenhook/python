n = int(input("请输入大于 1 的整数："))
if(n == 2):
    print("2 是质数！")
else:
    for i in range(2, n):
        if(n % i == 0):
            print("%d 不是质数！" % n)
            break
    else:
        print("%d 是质数！" % n)