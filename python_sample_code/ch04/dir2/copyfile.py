import os
cur_path=os.path.dirname(__file__) # 取得当前路径  
os.system("cls")  # 清除屏幕
os.system("mkdir dir2")  # 建立 dir2 目录
os.system("copy ossystem.py dir2\copyfile.py") # 复制文件 
file=cur_path + "\dir2\copyfile.py" 
os.system("notepad " + file)  # 以记事本开启 copyfile.py 文件
