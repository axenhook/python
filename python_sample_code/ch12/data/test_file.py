'''
模式有

r - 读取(文件需存在)

w - 新建文件写入(文件可不存在，若存在则清空)

a - 数据附加到旧文件后面(光标指在EOF)
'''

f = open('A.txt', 'a', encoding = 'UTF-8')   # 也可使用指定路径等方式，如： C:\A.txt
f.write('你好1\n')
f.write('你好2\n')
f.write('你好3\n')
f.close()


'''
Hello world
Today id a nice day!
'''


f=open('test_file.txt')
print(f.readline())
print(f.readline())
#f.close()


f.seek(0)
for line in f:
    print(line.strip())
    
f.close()

with open("test_file.txt") as f:
    for line in f:
        print(line.strip())          

# write to test_write.txt
# Write a file
with open("test_write.txt", "w") as out_file:
    out_file.write("This Text is going to out file\nLook at it and see!")
