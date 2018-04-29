def calsum(*params):
    total = 0
    for param in params:
        total += param
    return total
    
print("不定参函数示例：")
print("2 个参数：4 + 5 = %d" % calsum(4,5))
print("3 个参数：4 + 5 + 12 = %d" % calsum(4,5,12))
print("4 个参数：4 + 5 + 12 + 8 = %d" % calsum(4,5,12,8))
