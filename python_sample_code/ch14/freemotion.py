import pygame, random, math
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("自由移动")
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255,255,255))
ball = pygame.Surface((30,30))  #建立矩形绘图区
ball.fill((255,255,255))  #矩形区域背景设为白色
pygame.draw.circle(ball, (0,0,255), (15,15), 15, 0)  #画一个蓝色球体
rect1 = ball.get_rect()  #取得球矩形区域
rect1.center = (random.randint(100,250),random.randint(150,250))  #球起始位置
x, y = rect1.topleft  #球左上角坐标
direction = random.randint(20,70)  #起始角度
radian = math.radians(direction)  #转为弪度
dx = 5 * math.cos(radian)  #球水平运动速度
dy = -5 * math.sin(radian)  #球垂直运动速度
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0,0))  #清除绘图窗口
    x += dx  #改变水平位置
    y += dy  #改变垂直位置
    rect1.center = (x,y)
    if(rect1.left <= 0 or rect1.right >= screen.get_width()):  #到达左右边界
        dx *= -1  #水平速度变号
    elif(rect1.top <= 5 or rect1.bottom >= screen.get_height()-5):  #到达上下边界
        dy *= -1  #垂直速度变号
    screen.blit(ball, rect1.topleft)
    pygame.display.update()
pygame.quit()
