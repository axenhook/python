import os
from win32com import client
word = client.gencache.EnsureDispatch('Word.Application')
word.Visible = 1
word.DisplayAlerts = 0
doc = word.Documents.Add()
range1 = doc.Range(0,0)  #文件起始处
range1.InsertAfter("这是测试第一行\n这是测试第二行\n")
range1.InsertAfter("这是测试第三行\n这是测试第四行\n")
range1.InsertBefore("第一次插入到文件最前方\n")
range1.InsertBefore("再次插入到文件最前方\n")
cpath = os.path.dirname(__file__)
doc.SaveAs(cpath + "\\media\\test1.docx")
#doc.Close()
#word.Quit()
