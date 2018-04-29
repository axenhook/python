import pygame
pygame.init()  #启动Pygame
screen = pygame.display.set_mode((640, 320))  #建立绘图窗口
pygame.display.set_caption("基本架构")  #绘图窗口标题
background = pygame.Surface(screen.get_size())  #建立画布
background = background.convert()
background.fill((255,255,255))  #画布为白色
screen.blit(background, (0,0))  #在绘图窗口绘制画布
pygame.display.update()  #更新绘图窗口
running = True
while running:  #创建循环来侦测鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #用户单击关闭按钮
            running = False
pygame.quit()  #关闭绘图窗口
