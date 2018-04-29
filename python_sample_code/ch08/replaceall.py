import os
from win32com import client
from win32com.client import constants
word = client.gencache.EnsureDispatch('Word.Application')
word.Visible = 0
word.DisplayAlerts = 0
runpath = os.path.dirname(__file__) + "\\replace"  #获取replace文件夹的路径
tree = os.walk(runpath)  #取得目录树
print("所有 Word 文件：")
for dirname, subdir, files in tree:
    allfiles = []   
    for file in files:  # 取得所有.docx .doc文件，存入allfiles列表中
        ext = file.split(".")[-1]  #取得文件名后缀
        if ext=="docx" or ext=="doc":  #取得所有.docx .doc文件
            allfiles.append(dirname + '\\' + file)  #加入allfiles列表     
         
    if len(allfiles) > 0:  #如果有符合条件的文件
        for dfile in allfiles:
            print(dfile)
            doc = word.Documents.Open(dfile)  #打开文件
            word.Selection.Find.ClearFormatting()
            word.Selection.Find.Replacement.ClearFormatting()
            word.Selection.Find.Execute("方法",False,False,False,False,False,True,constants.wdFindContinue,False,"method",constants.wdReplaceAll)
            doc.Close()
word.Quit()
