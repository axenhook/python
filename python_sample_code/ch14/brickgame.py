import pygame, random, math, time

class Ball(pygame.sprite.Sprite):  #球体角色
    dx = 0  #x位移量
    dy = 0  #y位移量
    x = 0  #球x坐标
    y = 0  #球y坐标
    direction = 0  #球移动方向
    speed = 0  #球移动速度
 
    def __init__(self, sp, srx, sry, radium, color):
        pygame.sprite.Sprite.__init__(self)
        self.speed = sp
        self.x = srx
        self.y = sry
        self.image = pygame.Surface([radium*2, radium*2])  #绘制球体背景区域
        self.image.fill((255,255,255))    #设置背景区域为白色(与游戏窗口背景色相同)
        pygame.draw.circle(self.image, color, (radium,radium), radium, 0)
        self.rect = self.image.get_rect()  #取得球体区域
        self.rect.center = (srx,sry)  #初始位置
        self.direction = random.randint(40,70)  #移动角度
 
    def update(self):  #球体移动
        radian = math.radians(self.direction)  #角度转为弧度
        self.dx = self.speed * math.cos(radian)  #球水平运动速度
        self.dy = -self.speed * math.sin(radian)  #球垂直运动速度
        self.x += self.dx  #计算球的新坐标
        self.y += self.dy
        self.rect.x = self.x  #移动球
        self.rect.y = self.y
        if(self.rect.left <= 0 or self.rect.right >= screen.get_width()-10):  #到达左右边界
            self.bouncelr()
        elif(self.rect.top <= 10):  #到达上边界
            self.rect.top = 10
            self.bounceup()
        if(self.rect.bottom >= screen.get_height()-10):  #到达下边界出界
            return True
        else:
            return False
 
    def bounceup(self):  #上边界反弹
        self.direction = 360 - self.direction

    def bouncelr(self):  #左右边界反弹
        self.direction = (180 - self.direction) % 360
            
class Brick(pygame.sprite.Sprite):  #方块角色
    def __init__(self, color, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([38, 13])  #方块38x13
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Pad(pygame.sprite.Sprite):  #滑板角色
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("media\\pad.png")  #滑板图片
        self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.x = int((screen.get_width() - self.rect.width)/2)  #滑板位置
        self.rect.y = screen.get_height() - self.rect.height - 20
 
    def update(self):  #滑板位置随鼠标移动
        pos = pygame.mouse.get_pos()  #取得鼠标坐标
        self.rect.x = pos[0]  #鼠标的x坐标
        if self.rect.x > screen.get_width() - self.rect.width:  #不要移出右边界
            self.rect.x = screen.get_width() - self.rect.width

def gameover(message):  #结束程序
    global running            
    text = font1.render(message, 1, (255,0,255))  #显示讯息
    screen.blit(text, (screen.get_width()/2-100,screen.get_height()/2-20))
    pygame.display.update()  #更新画面
    time.sleep(3)  #暂停3秒
    running = False  #结束程序

pygame.init()
score = 0  #得分
font = pygame.font.SysFont("SimHei", 20)  #设置下方提示信息的字体
font1 = pygame.font.SysFont("SimHei", 32)  #结束程序信息字体
soundhit = pygame.mixer.Sound("media\\hit.wav")  #碰到方块的声音
soundpad = pygame.mixer.Sound("media\\pad.wav")  #碰到滑板的声音
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("俄罗斯方块游戏")
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255,255,255))
allsprite = pygame.sprite.Group()  #建立全部角色组
bricks = pygame.sprite.Group()  #建立砖块角色组
ball = Ball(5, 300, 350, 10, (255,0,0))  #建立红色球对象
allsprite.add(ball)  #加入全部角色组
pad = Pad()  #建立滑板对象
allsprite.add(pad)  #加入全部角色组
clock = pygame.time.Clock()
for row in range(0, 4):  #3行方块
    for column in range(0, 15):  #每行15个方块
        if row == 0 or row == 1:  #1,2行为绿色方块
            brick = Brick((0,255,0), column * 40 + 1, row * 15 + 1)
        if row == 2 or row == 3:  #3,4行为蓝色方块
            brick = Brick((0,0,255), column * 40 + 1, row * 15 + 1)
        bricks.add(brick)  #加入方块角色组
        allsprite.add(brick)  #加入全部角色组
msgstr = "单击鼠标左键开始游戏！"  #提示信息
playing = False  #开始时球不会移动
running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    buttons = pygame.mouse.get_pressed()  #或取鼠标按键状态
    if buttons[0]:  #单击鼠标左键后球可移动
        playing = True
    if playing == True:  #游戏进行中
        screen.blit(background, (0,0))  #清除绘图窗口
        fail = ball.update()  #移动球体
        if fail:  #球出界
            gameover("失败，再接再励！")
        pad.update()  #更新滑板位置
        hitbrick = pygame.sprite.spritecollide(ball, bricks, True)  #检查球和方块碰撞
        if len(hitbrick) > 0:  #球和方块发生碰撞
            score += len(hitbrick)  #计算分数
            soundhit.play()  #球撞方块声
            ball.rect.y += 20  #球向下移
            ball.bounceup()  #球反弹
            if len(bricks) == 0:  #所有方块消失
                gameover("恭喜，挑战成功！")
        hitpad = pygame.sprite.collide_rect(ball, pad)  #检查球和滑板碰撞
        if hitpad:  #球和滑板发生碰撞
            soundpad.play()  #球撞滑板声音
            ball.bounceup()  #球反弹
        allsprite.draw(screen)  #绘制所有角色
        msgstr = "得分：" + str(score)
    msg = font.render(msgstr, 1, (255,0,255))
    screen.blit(msg, (screen.get_width()/2-60,screen.get_height()-20))  #显示信息
    pygame.display.update()
pygame.quit()
