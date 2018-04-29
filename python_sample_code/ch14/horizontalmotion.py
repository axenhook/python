import pygame
pygame.init()
screen = pygame.display.set_mode((640, 70))
pygame.display.set_caption("水平移动")
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255,255,255))
ball = pygame.Surface((30,30))  #建立矩形绘图区
ball.fill((255,255,255))  #矩形区背景为白色
pygame.draw.circle(ball, (0,0,255), (15,15), 15, 0)  #画一个蓝色球
rect1 = ball.get_rect()  #取得球矩形区域
rect1.center = (320,45)  #球起始位置
x, y = rect1.topleft  #球左上角坐标
dx = 3  #球运动速度
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(30)  #每秒执行30次
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0,0))  #清除绘图窗口
    x += dx  #改变水平位置
    rect1.center = (x,y)
    if(rect1.left <= 0 or rect1.right >= screen.get_width()):  #到达左右边界
        dx *= -1
    screen.blit(ball, rect1.topleft)
    pygame.display.update()
pygame.quit()
