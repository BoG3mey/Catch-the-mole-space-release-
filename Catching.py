#Подключение модулей--------------------------------------------------
import pygame
from pygame.constants import HIDDEN 
from random import randint
import config
#Стат переменные--------------------------------------------------
run = True
lobbyrun = True
endgame = False
w = config.w
ws = config.ws
hs = config.hs
p1 = pygame.transform.scale(pygame.image.load('1.png'), (w,w))
p2 = pygame.transform.scale(pygame.image.load('2.png'), (w,w))
p3 = pygame.transform.scale(pygame.image.load('3.png'), (w,w))
p4 = pygame.transform.scale(pygame.image.load('4.png'), (w,w))
p5 = pygame.transform.scale(pygame.image.load('5.png'), (w,w))
p6 = pygame.transform.scale(pygame.image.load('6.png'), (w,w))
p7 = pygame.transform.scale(pygame.image.load('7.png'), (w,w))
p8 = pygame.transform.scale(pygame.image.load('8.png'), (w,w))
p9 = pygame.transform.scale(pygame.image.load('9.png'), (w,w))
plaser = pygame.transform.scale(pygame.image.load('laser.png'), (10,10))
hp = pygame.transform.scale(pygame.image.load('hp.png'), (50,50))
star1 = pygame.transform.scale(pygame.image.load('hp.png'), (5,5))
star2 = pygame.transform.scale(pygame.image.load('hp.png'), (5,5))
lobby = pygame.transform.scale(pygame.image.load('lobby.png'), (500,500))
class Asteroid():
    def __init__(self, x, y, w):
        self.have = True
        self.w = w
        self.x = x
        self.y = y
        self.grow = 20
        self.r = (self.x, self.y, self.w, self.w)
        self.random = randint(1,1)
        if self.random == 1:
            self.form = pygame.transform.scale(pygame.image.load('11.png'), (self.w, self.w))
    def show(self):
        if self.have == True:
            if astr.grow == 0 and self.w != 0:
                self.w -= 20
                if self.w < 100:
                    self.x += 10
                    self.y += 10
                self.r = (self.x, self.y, self.w, self.w)
                self.grow = 10
                if self.w == 0:
                    global HaveNowAstr
                    for i in TimesToSpawnAstr:
                        if i.time == -1:
                            i.time = randint(50,150)
                    HaveNowAstr -= 1
                    global Life
                    Life -= 1
                    self.have = False
                if self.random == 1:
                    self.form = pygame.transform.scale(pygame.image.load('11.png'), (self.w, self.w))
            scr.blit(self.form, self.r)
    def TimeToGrow(self):
        if self.have == True:
            if self.grow != 0:
                self.grow -= 1
    def Hitbox(self):
        if self.have == True:
            self.hitbox = pygame.draw.rect(scr, (255,0,0), self.r)
class TimesToSpawn():
    def __init__(self, time):
        self.time = time
class Star():
    def __init__(self):
        self.x = randint(0, ws)
        self.y = randint(0, hs)
        self.time = randint(50, 100)
        self.randform = randint(1,2)
        if self.randform == 1:
            self.form = star1
        if self.randform == 2:
            self.form = star2
HaveNowAstr = 0
AstrSize = config.AstrSize
AstrX = 50
AstrY = 50
Score = 0
Asteroids = []
MaxHaveNowAstr = 1
TimesToSpawnAstr = []
DefaultTimeToSpawn = config.DefaultTimeToSpawn
Life = config.Life
stars = []
CountOfStar = config.CountOfStar
for i in range(CountOfStar):
    stars.append(Star())
#Создание окна--------------------------------------------------
pygame.init()
scr = pygame.display.set_mode((ws, hs))
pygame.display.set_caption('Maded by abik')
pygame.init()
pygame.mouse.set_visible(False)
TimesToSpawnAstr.append(TimesToSpawn(DefaultTimeToSpawn))
#----------------------------------------------------------
while lobbyrun:
    pygame.time.delay(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lobbyrun = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            lobbyrun = False
    pygame.draw.rect(scr, (26, 30, 61), (0, 0, ws, hs))
    scr.blit(lobby,(250, 250, 500, 500))
    for i in stars:
        scr.blit(i.form, (i.x, i.y, 5, 5))
        if i.time != 0:
            i.time -= 1
        if i.time == 0:
            i.x = randint(0, ws)
            i.y = randint(0, hs)
            i.time = randint(50, 100)
            i.randform = randint(1,2)
            if i.randform == 1:
                i.form = star1
            if i.randform == 2:
                i.form = star2
    pos = pygame.mouse.get_pos()
    rlaser = pos + (5, 5)
    laser = pygame.draw.rect(scr, (255,0,0), rlaser)
    pygame.display.update()
#Цикл игры--------------------------------------------------
while run:
    pygame.time.delay(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in Asteroids:
                if laser.colliderect(i.hitbox):
                    Asteroids.remove(i)
                    for i in TimesToSpawnAstr:
                        if i.time == -1:
                            i.time = randint(50,150)
                    HaveNowAstr -= 1
                    Score += 1
    #--------------------------------------------------
    if Score > 5 and Score < 20:
        if MaxHaveNowAstr == 1:
            MaxHaveNowAstr = 2
            if len(TimesToSpawnAstr) == 1:
                TimesToSpawnAstr.append(TimesToSpawn(DefaultTimeToSpawn))
            print('Now you have 2 Astr!')
    if Score < 5:
        if MaxHaveNowAstr == 2:
            MaxHaveNowAstr = 1
            if len(TimesToSpawnAstr) == 2:
                TimesToSpawnAstr.pop[0]
            print('Now you have 1 Astr!')
    if Score > 20 and Score < 50:
        if MaxHaveNowAstr == 2:
            MaxHaveNowAstr = 3
            if len(TimesToSpawnAstr) == 2:
                TimesToSpawnAstr.append(TimesToSpawn(DefaultTimeToSpawn))
            print('Now you have 3 Astr!')
    if Score < 20 and Score > 5:
        if MaxHaveNowAstr == 3:
            MaxHaveNowAstr = 2
            if len(TimesToSpawnAstr) == 3:
                TimesToSpawnAstr.pop[0]
            print('Now you have 2 Astr!')
    if Score > 50:
        if MaxHaveNowAstr == 3:
            MaxHaveNowAstr = 4
            if len(TimesToSpawnAstr) == 3:
                TimesToSpawnAstr.append(TimesToSpawn(DefaultTimeToSpawn))
            print('Now you have 4 Astr!')
    if Score < 50 and Score > 20:
        if MaxHaveNowAstr == 4:
            MaxHaveNowAstr = 3
            if len(TimesToSpawnAstr) == 4:
                TimesToSpawnAstr.pop[0]
            print('Now you have 3 Astr!')
    if Score > 100:
        print('You Win!')    
        endgame = True
    if Life <= 0:
        run = False
    pos = pygame.mouse.get_pos()
    rlaser = pos + (5, 5)
    for i in TimesToSpawnAstr:
        if i.time != -1:
            i.time -= 1
        if i.time == 0 and HaveNowAstr < MaxHaveNowAstr:
            i.time -= 1
            a = randint(1,9)
            if a == 1:
                astr = Asteroid(100 + AstrX, 100 + AstrY, AstrSize)
            if a == 2:
                astr = Asteroid(400 + AstrX, 100 + AstrY, AstrSize)
            if a == 3:
                astr = Asteroid(700 + AstrX, 100 + AstrY, AstrSize)
            if a == 4:
                astr = Asteroid(100 + AstrX, 400 + AstrY, AstrSize)
            if a == 5:
                astr = Asteroid(400 + AstrX, 400 + AstrY, AstrSize)
            if a == 6:
                astr = Asteroid(700 + AstrX, 400 + AstrY, AstrSize)
            if a == 7:
                astr = Asteroid(100 + AstrX, 700 + AstrY, AstrSize)
            if a == 8:
                astr = Asteroid(400 + AstrX, 700 + AstrY, AstrSize)
            if a == 9:
                astr = Asteroid(700 + AstrX, 700 + AstrY, AstrSize)
            Asteroids.append(astr)
            HaveNowAstr += 1
            print('Astr created!')
    #Отрисовка--------------------------------------------------
    for i in Asteroids:
        if i.have == True:
            i.Hitbox()
    r1 = (100,100, w, w)
    r2 = (400,100, w, w)
    r3 = (700,100, w, w)
    r4 = (100,400, w, w)
    r5 = (400,400, w, w)
    r6 = (700,400, w, w)
    r7 = (100,700, w, w)
    r8 = (400,700, w, w)
    r9 = (700,700, w, w)
    pygame.draw.rect(scr, (26, 30, 61), (0, 0, ws, hs))
    for i in stars:
        scr.blit(i.form, (i.x, i.y, 5, 5))
        if i.time != 0:
            i.time -= 1
        if i.time == 0:
            i.x = randint(0, ws)
            i.y = randint(0, hs)
            i.time = randint(50, 100)
            i.randform = randint(1,2)
            if i.randform == 1:
                i.form = star1
            if i.randform == 2:
                i.form = star2
    scr.blit(p1,r1)
    scr.blit(p2,r2)
    scr.blit(p3,r3)
    scr.blit(p4,r4)
    scr.blit(p5,r5)
    scr.blit(p6,r6)
    scr.blit(p7,r7)
    scr.blit(p8,r8)
    scr.blit(p9,r9)
    for i in Asteroids:
        if i.have == True:
            i.show()
            i.TimeToGrow()
    laser = pygame.draw.rect(scr, (255,0,0), rlaser)
    f1 = pygame.font.Font(None, 72)
    text1 = f1.render(str(Score), 1, (10, 194, 250))
    scr.blit(text1, (ws/2, 10))
    hpg = 0
    for i in range(Life):
        scr.blit(hp, (0 + hpg, 0, 50, 50))
        hpg += 50
    #Обновление екрана--------------------------------------------------
    pygame.display.update()
while endgame:
    pygame.time.delay(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            endgame = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            lobbyrun = False
    pygame.draw.rect(scr, (26, 30, 61), (0, 0, ws, hs))
    scr.blit(lobby,(250, 250, 500, 500))
    for i in stars:
        scr.blit(i.form, (i.x, i.y, 5, 5))
        if i.time != 0:
            i.time -= 1
        if i.time == 0:
            i.x = randint(0, ws)
            i.y = randint(0, hs)
            i.time = randint(50, 100)
            i.randform = randint(1,2)
            if i.randform == 1:
                i.form = star1
            if i.randform == 2:
                i.form = star2
    pos = pygame.mouse.get_pos()
    rlaser = pos + (5, 5)
    laser = pygame.draw.rect(scr, (255,0,0), rlaser)
    f1 = pygame.font.Font(None, 270)
    text1 = f1.render('You Win!', 1, (255, 0, 0))
    scr.blit(text1, (100, hs/2))
    pygame.display.update()