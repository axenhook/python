import subprocess
ocr = subprocess.Popen("tesseract media\\text1.jpg media\\result")
ocr.wait()
text = open("media\\result.txt").read().strip()
print(text)
