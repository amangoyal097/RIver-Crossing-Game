import pygame
from config import GlobalThings
g = GlobalThings()
g.transform()
pygame.init()
pygame.display.set_caption("River crossing")


class Player(object):
    def __init__(self, x, y, width,
                 height, ingame,
                 score, obsno, level, life):   # constructor for objects
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 3   # initial velocity
        self.ingame = ingame
        self.score = score
        self.obsno = obsno
        self.level = level
        self.time = 30
        self.life = life

    def draw(self, p):   # drawing player and its arena
        if p == "p1":
            g.scr.blit(g.strt, (0, 910))
            g.scr.blit(g.fin, (0, 0))
            playerdisplay = g.fontobj.render("Player 1", 1, g.pcolor)
            obj = pygame.transform.scale(g.p1img, (self.width, self.height))
            i = 0
            x = 1290
            while i < p1.life:
                g.scr.blit(g.life, (x, 960))
                x += 45
                i += 1
        elif p == "p2":
            g.scr.blit(g.strt, (0, 0))
            g.scr.blit(g.fin, (0, 910))
            playerdisplay = g.fontobj.render("Player 2", 1, g.pcolor)
            obj = pygame.transform.scale(g.p2img, (self.width, self.height))
            i = 0
            x = 1290
            while i < p2.life:
                g.scr.blit(g.life, (x, 960))
                x += 45
                i += 1
        scoredisplay = g.fontobj.render("Score:" + str(self.score),
                                        1, g.scorecolor)
        timedisplay = g.fontobj.render(
            "Time:" + str(self.time),
            1, (0, 121, 68))
        g.scr.blit(obj, (self.x, self.y))
        g.scr.blit(scoredisplay, (1000, 20))
        g.scr.blit(timedisplay, (1250, 20))
        g.scr.blit(playerdisplay, (1270, 920))


class Movobstacle(object):   # class for moving obsracles
    def __init__(self, x, y, left, right):
        self.x = x
        self.y = y
        self.height = 60
        self.width = 120
        self.vel = 0
        self.right = right
        self.left = left

    def start(self):    # condition for bouncing of obstacles of the end
        if self.x <= 0:
            self.left = False
            self.right = True
        elif self.x >= g.swidth - self.vel - self.width:
            self.left = True
            self.right = False

# checking condition and moving obstacles in appropriate directions
    def move(self):
        if(self.x + self.y > 0):
            if self.left is True:
                self.x -= self.vel
            elif self.right is True:
                self.x += self.vel

    def draw(self):   # drawing obstacles on screen
        ob = pygame.transform.scale(g.obm, (self.width, self.height))
        g.scr.blit(ob, (self.x, self.y))


class Fixedobstacle(object):  # class for fixed obstacles
    def __init__(self, fwidth, fheight, fx, fy):
        self.fheight = fheight
        self.fwidth = fwidth
        self.fx = fx
        self.fy = fy

    def draw(self):  # drawing fixed obstacles
        ob = pygame.transform.scale(g.obf, (self.fwidth, self.fheight))
        g.scr.blit(ob, (self.fx, self.fy))


class Slab(object):   # partioon class
    def __init__(self, height, width):
        self.height = height
        self.width = width


# global objects
p1 = Player(650, 920, 100, 70, True, 0, 4, 1, 3)  # player 1
p2 = Player(650, 0, 100, 70, True, 0, 0, 1, 3)    # plyaer 2
division = Slab(70, 1500)                    # partition
movobs = []                                # arrays for
fixobs = []                                # obstacles

# adding obstacles to their arrays
height = 110
movobs.append(Movobstacle(0, height, False, True))
movobs.append(Movobstacle(g.swidth, height, False, True))
height += 108 + division.height
movobs.append(Movobstacle(200, height, True, False))
movobs.append(Movobstacle(700, height, True, False))
height += 108 + division.height
movobs.append(Movobstacle(500, height, True, False))
movobs.append(Movobstacle(850, height, True, False))
movobs.append(Movobstacle(g.swidth, height, True, False))
height += 108 + division.height
movobs.append(Movobstacle(400, height, False, True))
movobs.append(Movobstacle(1000, height, False, True))
height += 108 + division.height
movobs.append(Movobstacle(100, height, False, True))
movobs.append(Movobstacle(400, height, False, True))
movobs.append(Movobstacle(g.swidth, height, False, True))


height = 90 + 108
fixobs.append(Fixedobstacle(130, 70, 50, height))
fixobs.append(Fixedobstacle(130, 70, 500, height))
fixobs.append(Fixedobstacle(130, 70, 1200, height))
height += 108 + division.height
fixobs.append(Fixedobstacle(130, 70, 450, height))
fixobs.append(Fixedobstacle(130, 70, 850, height))
height += 108 + division.height
fixobs.append(Fixedobstacle(130, 70, 1200, height))
fixobs.append(Fixedobstacle(130, 70, 200, height))
fixobs.append(Fixedobstacle(130, 70, 700, height))
height += 108 + division.height
fixobs.append(Fixedobstacle(130, 70, 1200, height))
fixobs.append(Fixedobstacle(130, 70, 100, height))

# initializing the starting of the game with player 1
start = "p1"
# function to check for collision


def check(p):
    PlayerRect = pygame.Rect(p.x, p.y + 10, p.width, p .height - 10)
    for obj in movobs:
        MObsRect = pygame.Rect(obj.x + 10, obj.y + 10, 100, 50)
        if MObsRect.colliderect(PlayerRect):
            return False
    for obj in fixobs:
        FObsRect = pygame.Rect(obj.fx, obj.fy, obj.fwidth, obj.fheight)
        if FObsRect.colliderect(PlayerRect):
            return False


# function to move player and update score
def movement(p, plyr):
    prevobs = p.obsno
    if move[pygame.K_LEFT] and p.x > p.vel:
        p.x -= p.vel
    if move[pygame.K_RIGHT] and p.x < g.swidth - p.width - p.vel:
        p.x += p.vel
    if move[pygame.K_UP] and p.y >= p.vel:
        p.y -= p.vel
    if move[pygame.K_DOWN] and p.y <= g.sheight - p.height - p.vel:
        p.y += p.vel
    height = 90 + 108 + 35
    if p.y < height:
        p.obsno = 0
    elif p.y < height + 108 + division.height:
        p.obsno = 1
    elif p.y < height + 2 * 108 + 2 * division.height:
        p.obsno = 2
    elif p.y < height + 3 * 108 + 3 * division.height:
        p.obsno = 3
    else:
        p.obsno = 4
    if plyr == "p2":
        if prevobs == 0 and p.obsno == 1:
            p.score += 10
        elif prevobs == 1 and p.obsno == 2:
            p.score += 10
        elif prevobs == 2 and p.obsno == 3:
            p.score += 10
        elif prevobs == 3 and p.obsno == 4:
            p.score += 10
    elif plyr == "p1":
        if prevobs == 4 and p.obsno == 3:
            p.score += 10
        elif prevobs == 3 and p.obsno == 2:
            p.score += 10
        elif prevobs == 2 and p.obsno == 1:
            p.score += 10
        elif prevobs == 1 and p.obsno == 0:
            p.score += 10


# function to draw background
def drawbackground():
    g.scr.fill(g.bgcolor)


# function to draw banks
def drawbank():
    bankh = 90
    pygame.draw.rect(g.scr, g.bankcolor,
                     (0, g.sheight - bankh, g.swidth, bankh))
    pygame.draw.rect(g.scr, g.bankcolor, (0, 0, g.swidth, bankh))


# function to draw partition
def drawslabs():
    height = 90 + 108
    pygame.draw.rect(g.scr, g.slabcolor,
                     (0, height, division.width, division.height))
    height += 108 + division.height
    pygame.draw.rect(g.scr, g.slabcolor,
                     (0, height, division.width, division.height))
    height += 108 + division.height
    pygame.draw.rect(g.scr, g.slabcolor,
                     (0, height, division.width, division.height))
    height += 108 + division.height
    pygame.draw.rect(g.scr, g.slabcolor,
                     (0, height, division.width, division.height))


# function to move and draw obstacles
def drawobstacles():
    for obj in movobs:
        obj.start()
    for obj in movobs:
        obj.draw()
    for obj in movobs:
        obj.move()
    for obj in fixobs:
        obj.draw()


def drawstrtscreen():   # draws the startscreen
    g.scr.blit(g.strtbg, (0, 0))
    display = g.fobj.render("Press Space To PLAY:", 1, g.scorecolor)
    g.scr.blit(display, (300, 900))
    pygame.display.update()
    while True:
        for event in pygame.event.get():   # records every event happened
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    g.strtscreen = False
                    return
            if event.type == pygame.QUIT:
                g.play = False
                return
            pygame.display.update()


def drawendscreen():  # draws the endscreen
    if p1.score > p2.score:
        winner = g.fobj.render("Player 1 Wins!", 1, g.wincolor)
    elif p2.score > p1.score:
        winner = g.fobj.render("Player 2 Wins!", 1, g.wincolor)
    else:
        winner = g.fobj.render("No Player Wins!", 1, g.wincolor)
    gameover = g.fobj.render("GAME OVER", 1, g.govercolor)
    display = g.fobj.render("Press Space To END:", 1, g.endcolor)
    play1 = g.fobj.render("Player 1:", 1, g.p1end)
    play1score = g.fobj.render(str(p1.score), 1, g.p1end)
    play2 = g.fobj.render("Player 2:", 1, g.slabcolor)
    play2score = g.fobj.render(str(p2.score), 1, g.slabcolor)
    g.scr.fill(g.msgbg)
    g.scr.blit(gameover, (500, 200))
    g.scr.blit(play1, (300, 400))
    g.scr.blit(play1score, (400, 500))
    g.scr.blit(play2, (900, 400))
    g.scr.blit(play2score, (1000, 500))
    g.scr.blit(display, (300, 800))
    g.scr.blit(winner, (400, 700))
    pygame.display.update()
    while True:
        for event in pygame.event.get():  # records every event happened
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    g.strtscreen = False
                    return
            if event.type == pygame.QUIT:
                g.play = False
                return
            pygame.display.update()


strttimer = True       # variable to initialize timer when player begins
if(g.strtscreen):
    drawstrtscreen()
while g.play:           # game loop
    for event in pygame.event.get():  # records every event happened
        if event.type == pygame.QUIT:
            g.play = False
    if(start == "p1") and p1.ingame:     # player 1 playing
        for obj in movobs:
            obj.vel = p1.level * 3
        if strttimer:
            p1.time = 30
            secondcount = 1000
            stime = pygame.time.get_ticks()
            strttimer = False
        move = pygame.key.get_pressed()
        movement(p1, "p1")
        drawbackground()
        drawbank()
        drawslabs()
        drawobstacles()
        currtime = pygame.time.get_ticks()
        # timer for player
        if currtime - stime > secondcount and p1.y > p1.vel:
            p1.time -= 1
            secondcount += 1000
            if p1.time == 0:
                p1.draw("p1")
                pygame.display.update()
                pygame.time.delay(2000)
                if p1.life == 0:
                    if p2.ingame:
                        start = "p2"
                        p2.x = 650
                        p2.y = 0
                        strttimer = False
                    p1.ingame = False
                else:
                    p1.life -= 1
                    p1.x = 650
                    p1.y = 920
                    p1.time = 30
                    strttimer = True
        p1.draw("p1")
        pygame.display.update()
        templay = check(p1)
        if templay is False:    # cheking if player collided
            g.fail()
            pygame.time.delay(2000)
            if p1.life == 0:
                if p2.ingame:
                    start = "p2"
                    p2.x = 650
                    p2.y = 0
                    strttimer = False
                p1.ingame = False
            else:
                p1.life -= 1
                p1.x = 650
                p1.y = 920
        # checking if player finished
        if(p1.y <= p1.vel):
            p1.level += 1
            p1.score += 10
            while p1.time >= 0:
                g.success()
                p1.score += 2
                pygame.time.delay(50)
                drawbackground()
                drawbank()
                drawslabs()
                for obj in movobs:
                    obj.draw()
                for obj in fixobs:
                    obj.draw()
                p1.draw("p1")
                pygame.display.update()
                if p1.time == 0:
                    break
                else:
                    p1.time -= 1
            if p1.time == 0:     # checking if timer is 0
                pygame.time.delay(500)
                if p2.ingame:
                    start = "p2"
                    p2.x = 650
                    p2.y = 0
                    strttimer = False
                else:
                    p1.x = 650
                    p1.y = 920
                    strttimer = True
        pygame.display.update()

    elif start == "p2" and p2.ingame:          # player 2 playing
        for obj in movobs:
            obj.vel = p2.level * 3
        if not strttimer:
            p2.time = 30
            secondcount = 1000
            stime = pygame.time.get_ticks()
            strttimer = True
        move = pygame.key.get_pressed()
        movement(p2, "p2")
        drawbackground()
        drawbank()
        drawslabs()
        drawobstacles()
        currtime = pygame.time.get_ticks()
        if currtime - stime > secondcount:                 # timer for player
            p2.time -= 1
            secondcount += 1000
            if p2.time == 0:
                p2.draw("p2")
                pygame.display.update()
                pygame.time.delay(2000)
                if p2.life == 0:
                    if p1.ingame:
                        start = "p1"
                        p1.x = 650
                        p1.y = 920
                        strttimer = True
                    p2.ingame = False
                else:
                    p2.life -= 1
                    p2.x = 650
                    p2.y = 0
                    p2.time = 30
                    strttimer = False
        p2.draw("p2")
        pygame.display.update()
        templay = check(p2)
        if templay is False:
            g.fail()
            pygame.time.delay(2000)
            if p2.life == 0:
                if p1.ingame:
                    start = "p1"
                    p1.x = 650
                    p1.y = 920
                    strttimer = True
                p2.ingame = False
            else:
                p2.life -= 1
                p2.x = 650
                p2.y = 0
        # checking if player finished
        if(p2.y >= g.sheight - p2.height - p2.vel):
            p2.level += 1
            p2.score += 10
            while p2.time >= 0:
                g.success()
                p2.score += 2
                pygame.time.delay(50)
                drawbackground()
                drawbank()
                drawslabs()
                for obj in movobs:
                    obj.draw()
                for obj in fixobs:
                    obj.draw()
                p2.draw("p2")
                pygame.display.update()
                if p2.time == 0:     # checking if timer is 0
                    break
                else:
                    p2.time -= 1
            if p2.time == 0:
                pygame.time.delay(500)
                if p1.ingame:
                    start = "p1"
                    p1.x = 650
                    p1.y = 920
                    strttimer = True
                else:
                    p2.x = 650
                    p2.y = 0
                    strttimer = False
        pygame.display.update()
    # if both player lost all their lives
    elif p2.ingame is False and p1.ingame is False:
        drawendscreen()
        g.play = False

pygame.quit()
