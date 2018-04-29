import os.path
cur_path=os.path.dirname(__file__) # 获取当前目录路径
print("当前目录路径为："+cur_path)

filename=os.path.abspath("ospath.py")
if os.path.exists(filename):
    print("完整路径名称：" + filename)
    print("文件大小：" , os.path.getsize(filename))
    
    basename=os.path.basename(filename)
    print("路径最后的文件名为：" + basename)
    
    dirname=os.path.dirname(filename)
    print("当前文件目录路径：" + dirname) 
    
    print("是否为目录：",os.path.isdir(filename))
    
    fullpath,fname=os.path.split(filename)
    print("目录路径：" + fullpath)
    print("文件名：" + fname)
    
    Drive,fpath=os.path.splitdrive(filename)
    print("盘名：" + Drive)
    print("路径名称：" + fpath)   
    
    fullpath = os.path.join(fullpath + "\\" + fname)
    print("合并路径= " + fullpath)
