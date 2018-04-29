n = int(input("请输入大楼的楼层数："))
print("本大楼具有的楼层为：")
if(n > 3):
    n += 1
for i in range(1, n+1):
    if(i==4):
        continue
    print(i, end=" ")
print()