import pygame
pygame.init()
screen = pygame.display.set_mode((640, 300))
pygame.display.set_caption("鼠标移动事件")
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255,255,255))
ball = pygame.Surface((30,30))  #建立球的矩形背景绘图区
ball.fill((255,255,255))  #矩形区域背景为白色
pygame.draw.circle(ball, (0,0,255), (15,15), 15, 0)  #画蓝色实心圆作为球体
rect1 = ball.get_rect()  #取得球的矩形背景区域
rect1.center = (320,150)  #设置球的起始位置
x, y = rect1.topleft  #球左上角坐标
clock = pygame.time.Clock()
running = True
playing = False  #开始时球不能移动
while running:
    clock.tick(30)  #每秒执行30次
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    buttons = pygame.mouse.get_pressed()
    if buttons[0]:  #按下左键后拖动鼠标球可移动
        playing = True
    elif buttons[2]:  #按下右键后拖动鼠标球不能移动
        playing = False
    if playing == True:  #球可移动状态
        mouses = pygame.mouse.get_pos()  #取得鼠标坐标
        rect1.centerx = mouses[0]  #把鼠标的x坐标作为球中心的X坐标
        rect1.centery = mouses[1] #把鼠标的y坐标作为球中心的y坐标
    screen.blit(background, (0,0))  #清除绘图窗口
    screen.blit(ball, rect1.topleft)  #重新绘制
    pygame.display.update()  #显示
pygame.quit()
