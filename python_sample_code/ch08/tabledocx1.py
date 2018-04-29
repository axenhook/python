import os
from win32com import client
word = client.gencache.EnsureDispatch('Word.Application')
word.Visible = 1
word.DisplayAlerts = 0
cpath=os.path.dirname(__file__)
doc = word.Documents.Open(cpath + "\\media\\clipgraph.docx")
data = [ ["型号", "尺寸", "颜色", "价格"], ["A8", "5.0英寸", "白色", "8000"], \
         ["A10", "5.5 英寸", "金黄", "22000"] ]
paragraphs = doc.Paragraphs      #读取所有段落
range1 = paragraphs(4).Range     #取第4段的起止范围
table = doc.Tables.Add(range1, 3, 4)    #在第4段之前插入一个3行4列表格
for i in range(1,table.Rows.Count+1):     #i取值分别为1~3。切记rang（）函数的特性
              print(i)
#    for j in range(1,table.Columns.Count+1):   #j取值分别为1~4
#        table.Cell(i,j).Range.Text = data[i-1][j-1]   #第一次会把data[0][0],即"型号"，插入Cell(1,1)
#table.Cell(2,3).Range.Font.Color = 0x0000FF   #设置第2行第3列单元格的字体颜色
#doc.Close()
#word.Quit()
