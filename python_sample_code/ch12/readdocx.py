import  docx
doc = docx.Document("简介.docx")
for p in doc.paragraphs:
    print(p.text)
