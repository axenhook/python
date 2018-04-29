import os
from win32com import client
from win32com.client import constants
word = client.gencache.EnsureDispatch('Word.Application')
word.Visible = 1
word.DisplayAlerts = 0
cpath=os.path.dirname(__file__)
doc = word.Documents.Open(cpath + "\\media\\clipgraph.docx")
paragraphs = doc.Paragraphs
range1 = paragraphs(1).Range  #第1段
range1.Style = constants.wdStyleHeading1
range1.Style.Font.Name = "标楷体"
range1.Style.Font.Color = 0xFF0000	  #蓝色
range1.Style.Font.Bold = 1  #Italic, Underline, Shadow, Outline

range2 = paragraphs(2).Range  #第2段
range2.Style = constants.wdStyleHeading3
range2.ParagraphFormat.Alignment = constants.wdAlignParagraphRight

range3 = paragraphs(3).Range  #第3段
range3.Style.Font.Size = "10"
#doc.Close()
#word.Quit()
