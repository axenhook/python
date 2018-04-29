def makeFace(facename, msg, endstr):
    print(msg)  #显示提示信息
    cv2.namedWindow("frame")
    cv2.waitKey(0)
    cap = cv2.VideoCapture(0)  #打开摄像头
    while(cap.isOpened()):  #如果摄像头处于打开状态，则...
        ret, img = cap.read()  #读取图像
        if ret == True:  #读取成功
            cv2.imshow("frame", img)  #显示图像
            k = cv2.waitKey(100)  #每0.1秒读一次键盘
            if k == ord("z") or k == ord("Z"):  #如果输入z
                cv2.imwrite(facename,img)  #把读取的img保存至facename文件
                image = cv2.imread(facename)  #读取刚刚保存的facename文件至image变量，作为下面人脸识别函数的参数
                faces = faceCascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30,30), flags = cv2.CASCADE_SCALE_IMAGE)
                (x, y, w, h) = (faces[0][0], faces[0][1], faces[0][2], faces[0][3])  #取出第一张人脸区域
                image1 = Image.open(facename).crop((x, y, x+w, y+h))  #抓取人脸区域的图像并存至image1变量
                image1 = image1.resize((200, 200), Image.ANTIALIAS)  #把取得的人脸区域的分辨率变为200x200
                image1.save(facename)  #把经过处理的人脸文件保存至facename文件
                break;
    cap.release()  #关闭摄像头
    cv2.destroyAllWindows()   #关闭窗口
    print(endstr)    
    return

import cv2, os, math, operator
from PIL import Image
from functools import reduce

casc_path = "C:\\ProgramData\\Anaconda3\\pkgs\\opencv3-3.1.0-py27_0\\Library\etc\\haarcascades\\haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(casc_path)  #创建识别对象
recogname = "media\\recogface.jpg"  #预存的人脸文件
loginname = "media\\loginface.jpg"  #登录者的人脸文件
os.system("cls")  #清屏
if(os.path.exists(recogname)):  #如果预存的人脸文件已存在
    msg = "按任意键创建登录人脸文件。\n摄像头打开后按z键进行拍照对比！"
    makeFace(loginname, msg, "")  #创建登录者人脸文件
    pic1 = Image.open(recogname)  #打开预存的人脸文件
    pic2 = Image.open(loginname)  #打开登录者人脸文件
    h1 = pic1.histogram()  #取预存片文件的直方图信息
    h2 = pic2.histogram()    #取登录者图片的直方图信息
    diff = math.sqrt(reduce(operator.add, list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1)) #计算两个图形差异度
    if(diff <= 100):  #若差度在100内，可通过验证
        print("通过验证，欢迎使用本系统！ diff=%4.2f" % diff)
    else:
        print("人脸错误，无法使用本系统！ diff=%4.2f" % diff)
else:  #如果预存的人脸文件不存在
    msg = "按任意键创建预存的人脸文件。\n摄像头打开后按z进行拍照！\n"
    endstr = "预存文件建立完成！"
    makeFace(recogname, msg, endstr)  #建立预存人脸文件
