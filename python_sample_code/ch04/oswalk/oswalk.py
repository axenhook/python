import os
cur_path=os.path.dirname(__file__) # 取得当前路径
sample_tree=os.walk(cur_path)
for dirname,subdir,files in sample_tree:
    print("文件路径：",dirname)
    print("目录列表：" , subdir)   
    print("文件列表：",files)
    print()
