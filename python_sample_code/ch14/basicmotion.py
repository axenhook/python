import pygame
pygame.init()
screen = pygame.display.set_mode((640, 320))
pygame.display.set_caption("动画基本架构")
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255,255,255))

clock = pygame.time.Clock()  #建立时间组件
running = True
while running:
    clock.tick(1)  #每秒执行30次
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0,0))  #清除绘图窗口

    pygame.display.update()  #更新绘图窗口
pygame.quit()  #关闭绘图窗口
