import os,shutil
cur_path=os.path.dirname(__file__) # 取得当前路径
destfile= cur_path + "\\" + "newfile.py"
shutil.copy("shutil.py",destfile )  # 文件复制
