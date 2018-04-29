import pygame, random, math

class Ball(pygame.sprite.Sprite):
    dx = 0  #x位移量
    dy = 0  #y位移量
    x = 0  #球x坐标
    y = 0  #球y坐标
 
    def __init__(self, speed, srx, sry, radium, color):
        pygame.sprite.Sprite.__init__(self)
        self.x = srx
        self.y = sry
        self.image = pygame.Surface([radium*2, radium*2])  #绘制球体背景区
        self.image.fill((255,255,255))
        pygame.draw.circle(self.image, color, (radium,radium), radium, 0)
        self.rect = self.image.get_rect()  #取得球体区域
        self.rect.center = (srx,sry)  #初始位置
        direction = random.randint(20,70)  #移动角度
        radian = math.radians(direction)  #角度转为弧度
        self.dx = speed * math.cos(radian)  #球水平运动速度
        self.dy = -speed * math.sin(radian)  #球垂直运动速度
 
    def update(self):
        self.x += self.dx  #计算球新余标
        self.y += self.dy
        self.rect.x = self.x  #移动球图形
        self.rect.y = self.y
        if(self.rect.left <= 0 or self.rect.right >= screen.get_width()):  #到达左右边界
            self.dx *= -1  #水平速度变符号
        elif(self.rect.top <= 5 or self.rect.bottom >= screen.get_height()-5):  #到达上下边界
            self.dy *= -1  #垂直速度变符号

    def collidebounce(self):
        self.dx *= -1
            
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("建立及使用角色")
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255,255,255))
allsprite = pygame.sprite.Group()  #建立角色组
ball1 = Ball(8, 100, 100, 15, (0,0,255))  #建立蓝色球对象
allsprite.add(ball1)  #加入角色群组
ball2 = Ball(6, 200, 250, 15, (255,0,0))  #建立红色球对象
allsprite.add(ball2)
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0,0))  #清除绘图窗口
    ball1.update()  #对象更新
    ball2.update()
    allsprite.draw(screen)
    result = pygame.sprite.collide_rect(ball1, ball2)  #侦测碰撞
    if result == True:
        ball1.collidebounce()
        ball2.collidebounce()
    pygame.display.update()
pygame.quit()
